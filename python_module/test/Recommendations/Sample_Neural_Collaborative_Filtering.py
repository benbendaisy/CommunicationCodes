import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd # For creating dummy data easily

# --- Configuration ---
class CFG:
    num_users = 100
    num_items = 50
    embedding_dim_gmf = 32 # Embedding dimension for GMF path
    embedding_dim_mlp = 32 # Embedding dimension for MLP path (can be same or different)
    mlp_hidden_layers = [64, 32, 16] # Sizes of hidden layers in MLP
    dropout_rate = 0.1
    learning_rate = 0.001
    batch_size = 16
    num_epochs = 20
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --- NCF Model ---
class NeuralCollaborativeFiltering(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim_gmf, embedding_dim_mlp, mlp_hidden_layers, dropout_rate):
        super(NeuralCollaborativeFiltering, self).__init__()

        self.num_users = num_users
        self.num_items = num_items
        self.embedding_dim_gmf = embedding_dim_gmf
        self.embedding_dim_mlp = embedding_dim_mlp
        self.mlp_hidden_layers = mlp_hidden_layers
        self.dropout_rate = dropout_rate

        # --- GMF Path ---
        self.user_embedding_gmf = nn.Embedding(num_embeddings=self.num_users, embedding_dim=self.embedding_dim_gmf)
        self.item_embedding_gmf = nn.Embedding(num_embeddings=self.num_items, embedding_dim=self.embedding_dim_gmf)

        # --- MLP Path ---
        self.user_embedding_mlp = nn.Embedding(num_embeddings=self.num_users, embedding_dim=self.embedding_dim_mlp)
        self.item_embedding_mlp = nn.Embedding(num_embeddings=self.num_items, embedding_dim=self.embedding_dim_mlp)

        # MLP Layers
        mlp_modules = []
        # Input to MLP is concatenation of user and item MLP embeddings
        input_size = self.embedding_dim_mlp * 2
        for hidden_size in self.mlp_hidden_layers:
            mlp_modules.append(nn.Linear(input_size, hidden_size))
            mlp_modules.append(nn.ReLU())
            mlp_modules.append(nn.Dropout(p=self.dropout_rate))
            input_size = hidden_size
        self.mlp_layers = nn.Sequential(*mlp_modules)

        # --- Prediction Layer (NeuMF - Neural Matrix Factorization style) ---
        # The output dimension of GMF is embedding_dim_gmf
        # The output dimension of MLP is the last hidden layer size (mlp_hidden_layers[-1])
        # We concatenate these two pathways
        self.predict_layer_input_dim = self.embedding_dim_gmf + self.mlp_hidden_layers[-1]
        self.predict_layer = nn.Linear(self.predict_layer_input_dim, 1)

        self._init_weights()

    def _init_weights(self):
        # Initialize embeddings with a normal distribution
        nn.init.normal_(self.user_embedding_gmf.weight, std=0.01)
        nn.init.normal_(self.item_embedding_gmf.weight, std=0.01)
        nn.init.normal_(self.user_embedding_mlp.weight, std=0.01)
        nn.init.normal_(self.item_embedding_mlp.weight, std=0.01)

        # Initialize MLP layers and prediction layer
        for m in self.mlp_layers:
            if isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                nn.init.zeros_(m.bias)
        nn.init.xavier_uniform_(self.predict_layer.weight)
        nn.init.zeros_(self.predict_layer.bias)


    def forward(self, user_indices, item_indices):
        # GMF Path
        user_embed_gmf = self.user_embedding_gmf(user_indices)
        item_embed_gmf = self.item_embedding_gmf(item_indices)
        gmf_output = user_embed_gmf * item_embed_gmf # Element-wise product

        # MLP Path
        user_embed_mlp = self.user_embedding_mlp(user_indices)
        item_embed_mlp = self.item_embedding_mlp(item_indices)
        mlp_input = torch.cat((user_embed_mlp, item_embed_mlp), dim=-1) # Concatenate
        mlp_output = self.mlp_layers(mlp_input)

        # Concatenate GMF and MLP outputs
        neumf_input = torch.cat((gmf_output, mlp_output), dim=-1)

        # Prediction
        logits = self.predict_layer(neumf_input)
        # For binary classification (e.g., interacted or not), use sigmoid
        # For rating prediction, you might not use sigmoid here and use a different loss (e.g., MSE)
        prediction = torch.sigmoid(logits)

        return prediction.squeeze() # Squeeze to remove last dim of size 1

# --- Dummy Dataset ---
class InteractionDataset(Dataset):
    def __init__(self, user_item_pairs, labels):
        self.user_item_pairs = user_item_pairs
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        user = self.user_item_pairs[idx][0]
        item = self.user_item_pairs[idx][1]
        label = self.labels[idx]
        return torch.tensor(user, dtype=torch.long), \
               torch.tensor(item, dtype=torch.long), \
               torch.tensor(label, dtype=torch.float)

# --- Training Function ---
def train_one_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    total_loss = 0.0
    for batch_idx, (users, items, labels) in enumerate(dataloader):
        users, items, labels = users.to(device), items.to(device), labels.to(device)

        optimizer.zero_grad()
        predictions = model(users, items)
        loss = criterion(predictions, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        if batch_idx % 5 == 0: # Print less frequently
            print(f"  Batch {batch_idx+1}/{len(dataloader)}, Loss: {loss.item():.4f}")

    return total_loss / len(dataloader)

# --- Main Execution ---
if __name__ == '__main__':
    print(f"Using device: {CFG.device}")

    # 1. Generate Dummy Data
    # Let's create some positive interactions and some negative samples
    num_interactions = CFG.num_users * CFG.num_items // 5 # Approx 20% density
    
    # Positive samples (users interacting with items)
    users_pos = np.random.randint(0, CFG.num_users, size=num_interactions)
    items_pos = np.random.randint(0, CFG.num_items, size=num_interactions)
    positive_pairs = list(set(zip(users_pos, items_pos))) # Ensure unique positive pairs
    
    # Negative samples (users NOT interacting with items)
    # A simple strategy: for each user, sample items they haven't interacted with.
    # For simplicity here, we'll just randomly sample pairs and assume most are negative if not in positives.
    # A more robust negative sampling strategy is needed for real applications.
    all_possible_pairs = set((u, i) for u in range(CFG.num_users) for i in range(CFG.num_items))
    negative_pairs_set = list(all_possible_pairs - set(positive_pairs))
    
    # Balance positive and negative samples for training (e.g., 1:1 or 1:4 ratio)
    # Here, let's try to get roughly equal numbers, capped by available negatives
    num_neg_samples = min(len(positive_pairs) * 1, len(negative_pairs_set)) # 1x negative samples
    
    if num_neg_samples > 0:
        neg_sample_indices = np.random.choice(len(negative_pairs_set), size=num_neg_samples, replace=False)
        negative_pairs_sampled = [negative_pairs_set[i] for i in neg_sample_indices]
    else:
        negative_pairs_sampled = []
        print("Warning: Not enough unique negative pairs to sample. Dataset might be too dense or small.")


    user_item_data = positive_pairs + negative_pairs_sampled
    labels = [1.0] * len(positive_pairs) + [0.0] * len(negative_pairs_sampled)

    if not user_item_data:
        print("Error: No data to train on. Exiting.")
        exit()
        
    print(f"Total training samples: {len(user_item_data)}")
    print(f"Positive samples: {len(positive_pairs)}, Negative samples: {len(negative_pairs_sampled)}")


    # Create Dataset and DataLoader
    dataset = InteractionDataset(user_item_data, labels)
    dataloader = DataLoader(dataset, batch_size=CFG.batch_size, shuffle=True, num_workers=0) # num_workers=0 for simplicity

    # 2. Initialize Model, Criterion, Optimizer
    model = NeuralCollaborativeFiltering(
        num_users=CFG.num_users,
        num_items=CFG.num_items,
        embedding_dim_gmf=CFG.embedding_dim_gmf,
        embedding_dim_mlp=CFG.embedding_dim_mlp,
        mlp_hidden_layers=CFG.mlp_hidden_layers,
        dropout_rate=CFG.dropout_rate
    ).to(CFG.device)

    criterion = nn.BCELoss() # Binary Cross Entropy Loss for binary classification
    optimizer = optim.Adam(model.parameters(), lr=CFG.learning_rate, weight_decay=1e-5) # Added weight decay

    # 3. Training Loop
    print("\nStarting NCF training...")
    for epoch in range(CFG.num_epochs):
        avg_epoch_loss = train_one_epoch(model, dataloader, criterion, optimizer, CFG.device)
        print(f"Epoch {epoch+1}/{CFG.num_epochs}, Average Training Loss: {avg_epoch_loss:.4f}")

    print("\nTraining finished.")

    # 4. Example: Making a prediction (Inference)
    model.eval() # Set model to evaluation mode
    with torch.no_grad(): # No need to track gradients for inference
        sample_user_idx = torch.tensor([0, 1, 0], dtype=torch.long).to(CFG.device) # Batch of 3 user indices
        sample_item_idx = torch.tensor([5, 10, 15], dtype=torch.long).to(CFG.device) # Batch of 3 item indices
        
        predictions = model(sample_user_idx, sample_item_idx)
        print(f"\nSample predictions for (user, item) pairs:")
        for i in range(len(sample_user_idx)):
            print(f"  User {sample_user_idx[i].item()}, Item {sample_item_idx[i].item()}: Predicted score = {predictions[i].item():.4f}")

        # Example: Get top K items for a user (simplified, not efficient for large num_items)
        target_user_idx = 0
        all_item_indices = torch.arange(CFG.num_items, device=CFG.device)
        target_user_indices_repeated = torch.full_like(all_item_indices, fill_value=target_user_idx)
        
        scores_for_user = model(target_user_indices_repeated, all_item_indices)
        top_k = 5
        top_k_scores, top_k_item_indices = torch.topk(scores_for_user, k=top_k)
        
        print(f"\nTop {top_k} recommended item indices for User {target_user_idx}:")
        for i in range(top_k):
            print(f"  Item {top_k_item_indices[i].item()} with score {top_k_scores[i].item():.4f}")