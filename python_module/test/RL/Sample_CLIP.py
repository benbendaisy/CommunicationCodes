import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

# --- Hyperparameters ---
EMBED_DIM = 128          # Dimension of the shared embedding space
IMAGE_FEATURE_DIM = 256  # Input dimension for dummy image features
TEXT_VOCAB_SIZE = 100    # Vocabulary size for dummy text
TEXT_MAX_LEN = 20        # Max length for dummy text sequences
TEXT_EMBED_DIM = 64      # Embedding dim for text tokens before LSTM/Transformer
BATCH_SIZE = 32
LEARNING_RATE = 1e-3
EPOCHS = 50
TEMPERATURE = 0.07       # Initial temperature (can be made learnable)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# --- 1. Simplified Image Encoder ---
class SimpleImageEncoder(nn.Module):
    def __init__(self, input_dim, output_embed_dim):
        super().__init__()
        # In a real CLIP, this would be a ResNet or ViT
        self.fc1 = nn.Linear(input_dim, input_dim // 2)
        self.fc2 = nn.Linear(input_dim // 2, output_embed_dim) # No projection head here, direct to intermediate embed

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x) # Outputting an intermediate image representation
        return x

# --- 2. Simplified Text Encoder ---
class SimpleTextEncoder(nn.Module):
    def __init__(self, vocab_size, text_embed_dim, output_embed_dim):
        super().__init__()
        # In a real CLIP, this would be a Transformer
        self.embedding = nn.Embedding(vocab_size, text_embed_dim)
        self.lstm = nn.LSTM(text_embed_dim, output_embed_dim // 2, batch_first=True, bidirectional=True)
        # Using //2 and bidirectional to get output_embed_dim from concatenated hidden states
        # Alternatively, just use output_embed_dim and take the last hidden state

    def forward(self, x):
        x = self.embedding(x) # (batch_size, seq_len, text_embed_dim)
        # For LSTM, we take the final hidden state (or average of all hidden states)
        # LSTM output: output, (h_n, c_n)
        # h_n shape: (num_layers * num_directions, batch, hidden_size)
        _, (h_n, _) = self.lstm(x)
        # Concatenate hidden states from both directions if bidirectional
        # h_n is (2, batch, output_embed_dim // 2) for bidirectional
        # We want (batch, output_embed_dim)
        text_features = torch.cat((h_n[0,:,:], h_n[1,:,:]), dim=1)
        # Or, if not bidirectional and taking last hidden state of last layer:
        # text_features = h_n[-1, :, :]
        return text_features


# --- 3. Projection Heads ---
# These project the unimodal embeddings into the shared multimodal space
class ProjectionHead(nn.Module):
    def __init__(self, input_embed_dim, output_embed_dim, dropout_prob=0.1):
        super().__init__()
        self.fc1 = nn.Linear(input_embed_dim, input_embed_dim * 2)
        self.fc2 = nn.Linear(input_embed_dim * 2, output_embed_dim)
        self.dropout = nn.Dropout(dropout_prob)
        self.layer_norm = nn.LayerNorm(output_embed_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.layer_norm(x) # Normalize embeddings
        return x

# --- 4. CLIP Model ---
class SimpleCLIP(nn.Module):
    def __init__(self, image_encoder, text_encoder, image_embed_dim, text_embed_dim, shared_embed_dim, temperature=TEMPERATURE):
        super().__init__()
        self.image_encoder = image_encoder
        self.text_encoder = text_encoder

        self.image_projection = ProjectionHead(image_embed_dim, shared_embed_dim)
        self.text_projection = ProjectionHead(text_embed_dim, shared_embed_dim) # text_embed_dim here is output of LSTM

        # Learnable temperature parameter
        self.logit_scale = nn.Parameter(torch.ones([]) * np.log(1 / temperature))

    def encode_image(self, image_features):
        image_intermediate_embed = self.image_encoder(image_features)
        image_embed = self.image_projection(image_intermediate_embed)
        return F.normalize(image_embed, p=2, dim=-1) # L2 normalize

    def encode_text(self, text_tokens):
        text_intermediate_embed = self.text_encoder(text_tokens)
        text_embed = self.text_projection(text_intermediate_embed)
        return F.normalize(text_embed, p=2, dim=-1) # L2 normalize

    def forward(self, image_features, text_tokens):
        image_embeddings = self.encode_image(image_features)
        text_embeddings = self.encode_text(text_tokens)

        # Cosine similarity as dot product of normalized embeddings
        # Scaled by learned temperature
        logits_per_image = self.logit_scale.exp() * image_embeddings @ text_embeddings.T
        logits_per_text = logits_per_image.T # Symmetric

        return logits_per_image, logits_per_text

# --- 5. Contrastive Loss ---
def contrastive_loss(logits_per_image, logits_per_text):
    # Targets: diagonal elements are the correct pairs
    batch_size = logits_per_image.shape[0]
    targets = torch.arange(batch_size, device=logits_per_image.device)

    loss_i = F.cross_entropy(logits_per_image, targets)
    loss_t = F.cross_entropy(logits_per_text, targets)
    loss = (loss_i + loss_t) / 2.0
    return loss

# --- Dummy Data Generation ---
def get_dummy_batch(batch_size, image_dim, vocab_size, max_len, device):
    # Dummy images (random features)
    dummy_images = torch.randn(batch_size, image_dim).to(device)

    # Dummy text (random integer sequences)
    seq_lengths = np.random.randint(1, max_len + 1, batch_size)
    dummy_texts = torch.zeros(batch_size, max_len, dtype=torch.long).to(device)
    for i in range(batch_size):
        dummy_texts[i, :seq_lengths[i]] = torch.randint(0, vocab_size, (seq_lengths[i],)).to(device)
    return dummy_images, dummy_texts

# --- Training Loop ---
if __name__ == "__main__":
    # Instantiate encoders
    image_enc = SimpleImageEncoder(IMAGE_FEATURE_DIM, EMBED_DIM).to(device) # output_embed_dim here is intermediate
    text_enc = SimpleTextEncoder(TEXT_VOCAB_SIZE, TEXT_EMBED_DIM, EMBED_DIM).to(device) # output_embed_dim here is intermediate

    # Instantiate CLIP model
    clip_model = SimpleCLIP(image_enc, text_enc, EMBED_DIM, EMBED_DIM, EMBED_DIM).to(device) # EMBED_DIM is for intermediate representation, final is also EMBED_DIM

    optimizer = optim.Adam(clip_model.parameters(), lr=LEARNING_RATE)
    losses = []

    print("Starting training...")
    for epoch in range(EPOCHS):
        clip_model.train()
        epoch_loss = 0
        num_batches = 50 # Simulate some batches per epoch

        for _ in range(num_batches):
            optimizer.zero_grad()
            images, texts = get_dummy_batch(BATCH_SIZE, IMAGE_FEATURE_DIM, TEXT_VOCAB_SIZE, TEXT_MAX_LEN, device)

            logits_img, logits_text = clip_model(images, texts)
            loss = contrastive_loss(logits_img, logits_text)

            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()

        avg_epoch_loss = epoch_loss / num_batches
        losses.append(avg_epoch_loss)
        if (epoch + 1) % 5 == 0:
            print(f"Epoch [{epoch+1}/{EPOCHS}], Loss: {avg_epoch_loss:.4f}, Logit Scale: {clip_model.logit_scale.exp().item():.4f}")

    print("Training finished.")

    # Plotting loss
    plt.figure(figsize=(10, 5))
    plt.plot(losses)
    plt.title("Training Loss Over Epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Average Contrastive Loss")
    plt.grid(True)
    plt.show()

    # --- Example: Zero-Shot Classification (Conceptual) ---
    print("\n--- Zero-Shot Classification Example ---")
    clip_model.eval()

    # 1. Create a dummy query image
    query_image_features, _ = get_dummy_batch(1, IMAGE_FEATURE_DIM, TEXT_VOCAB_SIZE, TEXT_MAX_LEN, device)

    # 2. Define some text prompts (class descriptions)
    # For our dummy text encoder, these also need to be random int sequences
    # In a real scenario: prompts = ["a photo of a cat", "a photo of a dog", "a drawing of a bird"]
    # Here, we'll generate dummy token sequences for them
    num_classes = 3
    class_prompts_tokens = []
    for _ in range(num_classes):
        _, text_tokens = get_dummy_batch(1, IMAGE_FEATURE_DIM, TEXT_VOCAB_SIZE, TEXT_MAX_LEN, device)
        class_prompts_tokens.append(text_tokens.squeeze(0)) # Remove batch dim

    # Manually create some "interpretable" prompts if desired (still dummy tokens)
    # These are just for illustration; their meaning is not learned with random data
    prompt_names = ["Class A (e.g., Cat-like)", "Class B (e.g., Dog-like)", "Class C (e.g., Bird-like)"]


    with torch.no_grad():
        # Encode the query image
        image_embedding = clip_model.encode_image(query_image_features) # (1, EMBED_DIM)

        # Encode the text prompts
        text_embeddings = []
        for tokens in class_prompts_tokens:
            text_embed = clip_model.encode_text(tokens.unsqueeze(0)) # Add batch dim
            text_embeddings.append(text_embed)
        text_embeddings_tensor = torch.cat(text_embeddings, dim=0) # (num_classes, EMBED_DIM)

        # 3. Compute cosine similarities between the image and all text prompts
        # image_embedding is (1, EMBED_DIM), text_embeddings_tensor is (num_classes, EMBED_DIM)
        # Similarities will be (1, num_classes)
        similarities = image_embedding @ text_embeddings_tensor.T
        probabilities = F.softmax(similarities, dim=1) # Convert to probabilities

    predicted_class_idx = probabilities.argmax().item()

    print(f"Query Image (random features): {query_image_features.mean().item():.2f} ...") # Just to show it's there
    print("Text Prompts (random token sequences):")
    for i, name in enumerate(prompt_names):
        print(f"  {name}: Prob {probabilities[0, i].item():.3f}")
    print(f"\nPredicted class for the dummy image: {prompt_names[predicted_class_idx]}")

    # Note: With random data and simple encoders, these "zero-shot" predictions
    # will be meaningless. The purpose is to show the *mechanism*.