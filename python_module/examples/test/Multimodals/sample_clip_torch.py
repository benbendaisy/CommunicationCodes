import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import models
from transformers import DistilBertModel, DistilBertTokenizer
from torch.utils.data import Dataset, DataLoader
import numpy as np

# --- Configuration ---
class CFG:
    embed_dim = 256  # Dimension of the shared embedding space
    batch_size = 4   # Keep small for a dummy dataset; must be <= num_samples
    num_epochs = 10
    learning_rate = 1e-4
    temperature = 0.07 # Fixed temperature for contrastive loss
    image_model_name = 'resnet18'
    text_model_name = 'distilbert-base-uncased'
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dummy_num_samples = 8 # Number of dummy image-text pairs
    image_size = 224

print(f"Using device: {CFG.device}")

# --- 1. Image Encoder ---
class ImageEncoder(nn.Module):
    def __init__(self, pretrained=True):
        super().__init__()
        if CFG.image_model_name == 'resnet18':
            weights = models.ResNet18_Weights.DEFAULT if pretrained else None
            self.model = models.resnet18(weights=weights)
        elif CFG.image_model_name == 'resnet50':
            weights = models.ResNet50_Weights.DEFAULT if pretrained else None
            self.model = models.resnet50(weights=weights)
        else:
            raise ValueError(f"Unsupported image model: {CFG.image_model_name}")

        # Modify the model to output features before the final classification layer
        self.model.fc = nn.Identity() # Output features from the layer before fc

    def forward(self, x):
        return self.model(x)

# --- 2. Text Encoder ---
class TextEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = DistilBertModel.from_pretrained(CFG.text_model_name)

    def forward(self, input_ids, attention_mask):
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        # Use the [CLS] token's representation (first token)
        last_hidden_state = outputs.last_hidden_state
        return last_hidden_state[:, 0, :] # [batch_size, hidden_dim]

# --- 3. Projection Head ---
class ProjectionHead(nn.Module):
    def __init__(self, input_dim, output_dim=CFG.embed_dim):
        super().__init__()
        self.projection = nn.Linear(input_dim, output_dim)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(output_dim, output_dim) # Optional: deeper projection
        # For simplicity, let's use a single linear layer + normalization as often done
        # self.projection = nn.Linear(input_dim, output_dim)
        # self.norm = nn.LayerNorm(output_dim)

    def forward(self, x):
        # Simple linear projection for this example
        projected = self.projection(x)
        # x = self.relu(projected) # Can add non-linearity
        # x = self.fc(x)
        # x = self.norm(x) # LayerNorm can help
        # CLIP often uses just a linear projection to the embedding dimension
        return F.normalize(projected, p=2, dim=-1) # Normalize embeddings

# --- 4. CLIP Model ---
class CLIPModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.image_encoder = ImageEncoder()
        self.text_encoder = TextEncoder()

        # Determine feature dimensions from encoders
        # ResNet18/50 output 512/2048 features before fc
        image_feature_dim = self.image_encoder.model.inplanes if CFG.image_model_name == 'resnet18' and hasattr(self.image_encoder.model, 'inplanes') and self.image_encoder.model.fc == nn.Identity() else \
                            (2048 if CFG.image_model_name == 'resnet50' else 512) # common output sizes
        # if resnet fc is Identity, inplanes isn't what we want. It's the output of the pooling layer.
        # For resnet18, it's 512. For resnet50, it's 2048.
        if CFG.image_model_name == 'resnet18': image_feature_dim = 512
        if CFG.image_model_name == 'resnet50': image_feature_dim = 2048

        text_feature_dim = self.text_encoder.model.config.hidden_size # e.g., 768 for distilbert

        self.image_projection = ProjectionHead(input_dim=image_feature_dim)
        self.text_projection = ProjectionHead(input_dim=text_feature_dim)
        self.temperature = CFG.temperature

    def forward(self, images, input_ids, attention_mask):
        image_features = self.image_encoder(images)
        text_features = self.text_encoder(input_ids, attention_mask)

        image_embeddings = self.image_projection(image_features)
        text_embeddings = self.text_projection(text_features)

        return image_embeddings, text_embeddings

    def calculate_loss(self, image_embeddings, text_embeddings):
        # Cosine similarity as logits
        # Normalized embeddings are assumed from ProjectionHead
        logits_per_image = torch.matmul(image_embeddings, text_embeddings.t()) / self.temperature
        logits_per_text = logits_per_image.t()

        batch_size = image_embeddings.shape[0]
        labels = torch.arange(batch_size, device=CFG.device) # Targets: 0, 1, ..., batch_size-1

        loss_img = F.cross_entropy(logits_per_image, labels)
        loss_text = F.cross_entropy(logits_per_text, labels)

        loss = (loss_img + loss_text) / 2.0
        return loss

# --- 5. Dummy Data ---
class DummyImageTextDataset(Dataset):
    def __init__(self, num_samples, image_size, tokenizer):
        self.num_samples = num_samples
        self.image_size = image_size
        self.tokenizer = tokenizer

        # Generate dummy images (random tensors)
        self.dummy_images = [torch.randn(3, image_size, image_size) for _ in range(num_samples)]

        # Generate dummy captions
        self.dummy_captions = [
            "a photo of a cat", "a drawing of a dog", "a picture of the sky",
            "an image of a car", "a red apple on a table", "a beautiful sunset",
            "a computer screen with code", "a person smiling happily"
        ] * (num_samples // 8 + 1) # Repeat if num_samples is large
        self.dummy_captions = self.dummy_captions[:num_samples]


    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        image = self.dummy_images[idx]
        caption = self.dummy_captions[idx]

        # Tokenize caption
        tokenized_caption = self.tokenizer(
            caption,
            padding='max_length',
            truncation=True,
            max_length=32, # Max sequence length for text
            return_tensors="pt"
        )
        input_ids = tokenized_caption['input_ids'].squeeze()
        attention_mask = tokenized_caption['attention_mask'].squeeze()

        return image, input_ids, attention_mask


# --- 6. Training Loop ---
def train_one_epoch(model, dataloader, optimizer, device):
    model.train()
    total_loss = 0.0

    for batch_idx, (images, input_ids, attention_mask) in enumerate(dataloader):
        images = images.to(device)
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)

        optimizer.zero_grad()

        image_embeddings, text_embeddings = model(images, input_ids, attention_mask)
        loss = model.calculate_loss(image_embeddings, text_embeddings)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        if batch_idx % 2 == 0: # Print less frequently for larger datasets
             print(f"  Batch {batch_idx+1}/{len(dataloader)}, Loss: {loss.item():.4f}")


    avg_loss = total_loss / len(dataloader)
    return avg_loss

# --- Main Execution ---
if __name__ == '__main__':
    # Initialize Tokenizer (must be done before creating dataset)
    text_tokenizer = DistilBertTokenizer.from_pretrained(CFG.text_model_name)

    # Create dummy dataset and dataloader
    dummy_dataset = DummyImageTextDataset(
        num_samples=CFG.dummy_num_samples,
        image_size=CFG.image_size,
        tokenizer=text_tokenizer
    )
    # Ensure batch size is not larger than dataset size for this dummy example
    actual_batch_size = min(CFG.batch_size, CFG.dummy_num_samples)
    if actual_batch_size == 0:
        print("No samples in dataset. Exiting.")
        exit()

    dummy_dataloader = DataLoader(
        dummy_dataset,
        batch_size=actual_batch_size,
        shuffle=True # Shuffle for training
    )

    # Initialize model, optimizer
    clip_model = CLIPModel().to(CFG.device)
    # You might want to only optimize projection heads or fine-tune everything
    optimizer = optim.AdamW(clip_model.parameters(), lr=CFG.learning_rate, weight_decay=1e-3)

    print("Starting CLIP dummy training...")
    for epoch in range(CFG.num_epochs):
        avg_epoch_loss = train_one_epoch(clip_model, dummy_dataloader, optimizer, CFG.device)
        print(f"Epoch {epoch+1}/{CFG.num_epochs}, Average Loss: {avg_epoch_loss:.4f}")

    print("Dummy training finished.")

    # --- Example: Getting embeddings (Inference) ---
    # This part demonstrates how to get embeddings after "training"
    # Note: The model is not meaningfully trained on this dummy data.
    clip_model.eval()
    with torch.no_grad():
        # Get a sample batch
        sample_images, sample_input_ids, sample_attention_mask = next(iter(dummy_dataloader))
        sample_images = sample_images.to(CFG.device)
        sample_input_ids = sample_input_ids.to(CFG.device)
        sample_attention_mask = sample_attention_mask.to(CFG.device)

        img_emb, txt_emb = clip_model(sample_images, sample_input_ids, sample_attention_mask)
        print(f"\nSample Image Embeddings shape: {img_emb.shape}")
        print(f"Sample Text Embeddings shape: {txt_emb.shape}")

        # Example: Calculate similarity for the first image with all texts in the batch
        similarities = torch.matmul(img_emb[0:1], txt_emb.t()) # Sim of 1st img with all texts
        print(f"Similarity of 1st image with batch texts: {similarities.squeeze().cpu().numpy()}")