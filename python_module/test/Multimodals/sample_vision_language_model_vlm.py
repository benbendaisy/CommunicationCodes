import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.models import resnet50
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from PIL import Image


# Load pre-trained vision model (ResNet-50)
vision_encoder = resnet50(pretrained=True)
# Remove the final classification layer to get image features
vision_encoder = nn.Sequential(*list(vision_encoder.children())[:-1])
vision_encoder.eval() # Set to evaluation mode

# Load pre-trained language model (GPT-2) and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# Set a padding token if it doesn't exist
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
language_model = GPT2LMHeadModel.from_pretrained('gpt2')
language_model.train() # Set to training mode for fine-tuning


class VisionLanguageModel(nn.Module):
    def __init__(self, vision_encoder, language_model, vision_embedding_dim=2048, language_embedding_dim=768):
        super(VisionLanguageModel, self).__init__()
        self.vision_encoder = vision_encoder
        self.language_model = language_model
        
        self.vision_projection = nn.Linear(vision_embedding_dim, language_embedding_dim)

    def forward(self, image_tensor, caption_ids, attention_mask=None):
        # Freeze vision encoder
        with torch.no_grad():
            image_features = self.vision_encoder(image_tensor)
            image_features = image_features.view(image_features.size(0), -1)
        
        image_embedding = self.vision_projection(image_features).unsqueeze(1)
        
        text_embeddings = self.language_model.transformer.wte(caption_ids)
        
        embeddings = torch.cat([image_embedding, text_embeddings], dim=1)
        
        # Create an updated attention mask
        if attention_mask is not None:
            prefix_attention_mask = torch.ones(image_embedding.size(0), 1).to(attention_mask.device)
            updated_attention_mask = torch.cat([prefix_attention_mask, attention_mask], dim=1)
        else:
            updated_attention_mask = None
        
        # ✨ --- START OF THE FIX --- ✨
        # Create labels that are the same size as the input embeddings
        # We will ignore the loss for the image part by setting its label to -100
        ignore_index = -100
        image_prefix_labels = torch.full(
            (image_embedding.size(0), 1), ignore_index, dtype=torch.long, device=caption_ids.device
        )
        
        # Concatenate the ignore labels with the actual caption labels
        labels = torch.cat([image_prefix_labels, caption_ids], dim=1)
        # ✨ --- END OF THE FIX --- ✨
            
        # Pass the combined embeddings and the new labels to the language model
        outputs = self.language_model(
            inputs_embeds=embeddings, 
            attention_mask=updated_attention_mask, 
            labels=labels  # Use the newly created labels
        )
        
        return outputs.loss


# --- Data Preparation (Dummy Example) ---
# Image preprocessing
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load a sample image (replace with your image path)
try:
    image = Image.open("/Users/bendaisyarthurannie/Downloads/vanilla.png").convert("RGB")
except FileNotFoundError:
    # Create a dummy image if not found
    image = Image.new('RGB', (224, 224), color = 'red')

image_tensor = preprocess(image).unsqueeze(0) # Add batch dimension

# Sample caption
caption = "vanilla flower"
caption_ids = tokenizer.encode(caption, return_tensors='pt')

# --- Training Setup ---
vlm = VisionLanguageModel(vision_encoder, language_model)
optimizer = torch.optim.Adam(list(vlm.vision_projection.parameters()) + list(vlm.language_model.parameters()), lr=5e-5)

# --- Training Loop (Simplified) ---
print("Starting training...")
for epoch in range(10): # Train for a few epochs
    optimizer.zero_grad()
    loss = vlm(image_tensor, caption_ids)
    if loss is not None:
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")
    else:
        print(f"Epoch {epoch+1}, Loss is None.")


def generate_caption(image_tensor, model, tokenizer, max_length=50):
    model.eval()
    with torch.no_grad():
        # Get image features
        image_features = model.vision_encoder(image_tensor)
        image_features = image_features.view(image_features.size(0), -1)
        
        # Project and get the initial embedding
        image_embedding = model.vision_projection(image_features).unsqueeze(1)
        
        # Use the language model's generate function
        # We start with the image embedding as the initial input
        output_ids = model.language_model.generate(
            inputs_embeds=image_embedding,
            max_length=max_length,
            num_beams=4, # Use beam search for better results
            early_stopping=True,
            pad_token_id=tokenizer.pad_token_id
        )
        
        # Decode the generated ids to a string
        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return caption

# Generate a caption for our sample image
generated_caption = generate_caption(image_tensor, vlm, tokenizer)
print(f"\nGenerated Caption: {generated_caption}")