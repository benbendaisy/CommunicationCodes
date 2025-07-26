import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding, self).__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-np.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        return x + self.pe[:x.size(0), :]

class TransformerModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers, num_heads, dropout):
        super(TransformerModel, self).__init__()
        self.embedding = nn.Linear(input_dim, hidden_dim)
        self.positional_encoding = PositionalEncoding(hidden_dim)
        encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=num_heads)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, src):
        embedded = self.embedding(src)
        embedded = self.positional_encoding(embedded)
        embedded = self.dropout(embedded)
        output = self.transformer_encoder(embedded)
        output = self.fc(output[-1, :, :])
        return output

# Example usage
input_dim = 100
hidden_dim = 128
output_dim = 10
num_layers = 2
num_heads = 4
dropout = 0.1

model = TransformerModel(input_dim, hidden_dim, output_dim, num_layers, num_heads, dropout)

# Example input
batch_size = 32
seq_len = 20
input_data = torch.randn(seq_len, batch_size, input_dim)  # Shape: (seq_len, batch_size, input_dim)

# Forward pass
output = model(input_data)
print(output.shape)  # Output shape: (batch_size, output_dim)