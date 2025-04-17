import torch
import torch.nn as nn
import torch.nn.functional as F
from math import sqrt

class MultiHeadAttention(nn.Module):
    def __init__(self, d_in, d_out, context_length, dropout, n_heads, okv_bias=False):
        super().__init__()
        assert d_in % n_heads == 0, "d_in must be divisible by n_heads"

        self.n_heads = n_heads
        self.d_in = d_in
        self.d_out = d_out
        self.context_length = context_length
        self.head_dim = d_in // n_heads
        
        self.query = nn.Linear(d_in, d_in, bias=okv_bias)
        self.key = nn.Linear(d_in, d_in, bias=okv_bias)
        self.value = nn.Linear(d_in, d_in, bias=okv_bias)
        self.fc_out = nn.Linear(d_in, d_out)

        self.dropout = nn.Dropout(dropout)

    def forward(self, input_embeddings):
        """
        input_embeddings: (B, T, D)
        B: batch size
        T: sequence length
        D: embedding dimension
        """
        B, T, D = input_embeddings.size()
        assert T == self.context_length, f"Input sequence length {T} does not match expected length {self.context_length}"
        assert D == self.d_in, f"Input embedding dimension {D} does not match expected dimension {self.d_in}"

        Q = self.query(input_embeddings)
        K = self.key(input_embeddings)
        V = self.value(input_embeddings)

        # Split heads
        def split_heads(x):
            # (B, T, D) → (B, n_heads, T, head_dim)
            x = x.view(B, T, self.n_heads, self.head_dim).transpose(1, 2)
        
        Q= split_heads(Q)
        K = split_heads(K)
        V = split_heads(V)

        # Scaled Dot-Product Attention
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) / sqrt(self.head_dim)

        # causal mask: prevent attending to future tokens
        # (B, H, T, T)
        causal_mask = torch.triu(torch.ones(T, T), diagonal=1).bool()
        attn_scores = attn_scores.masked_fill(causal_mask, float('-inf'))

        attn_probs = F.softmax(attn_scores, dim=-1)
        attn_probs = self.dropout(attn_probs)

        attn_output = torch.matmul(attn_probs, V) # (B, H, T, Head_dim)
        
        # merge heads
        attn_output = attn_output.transpose(1, 2).contiguous().view(B, T, D)

        return self.fc_out(attn_output)