import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from typing import Optional, Tuple

class GraphConv(nn.Module):
    """Graph Convolutional Layer for Graphomer"""
    def __init__(self, in_features: int, out_features: int):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.root_emb = nn.Embedding(1, out_features)
        
    def forward(self, x: Tensor, adj: Tensor) -> Tensor:
        """
        Args:
            x: Node features [batch_size, num_nodes, in_features]
            adj: Adjacency matrix [batch_size, num_nodes, num_nodes]
        Returns:
            Output features [batch_size, num_nodes, out_features]
        """
        batch_size, num_nodes, _ = x.shape
        
        # Message passing
        out = torch.bmm(adj, x)
        
        # Transform features
        out = self.linear(out)
        
        # Add root embedding
        root_idx = torch.zeros(batch_size, dtype=torch.long, device=x.device)
        root_emb = self.root_emb(root_idx).unsqueeze(1)  # [batch_size, 1, out_features]
        root_emb = root_emb.expand(-1, num_nodes, -1)
        
        out += root_emb
        return out

class Expert(nn.Module):
    """Single Expert in MoE Layer"""
    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)
        self.activation = nn.GELU()
        
    def forward(self, x: Tensor) -> Tensor:
        return self.linear2(self.dropout(self.activation(self.linear1(x))))

class MoELayer(nn.Module):
    """Mixture of Experts Layer"""
    def __init__(self, d_model: int, d_ff: int, num_experts: int, top_k: int = 2, dropout: float = 0.1):
        super().__init__()
        self.d_model = d_model
        self.num_experts = num_experts
        self.top_k = top_k
        
        # Create experts
        self.experts = nn.ModuleList([Expert(d_model, d_ff, dropout) for _ in range(num_experts)])
        self.gate = nn.Linear(d_model, num_experts, bias=False)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x: Tensor) -> Tensor:
        """
        Args:
            x: Input tensor [batch_size, seq_len, d_model]
        Returns:
            Output tensor [batch_size, seq_len, d_model]
        """
        batch_size, seq_len, _ = x.shape
        
        # Reshape for expert processing
        x_flat = x.reshape(-1, self.d_model)  # [batch_size * seq_len, d_model]
        
        # Compute gate scores
        gate_scores = self.gate(x_flat)  # [batch_size * seq_len, num_experts]
        gate_probs = F.softmax(gate_scores, dim=-1)
        
        # Select top-k experts
        top_k_gate_probs, top_k_indices = torch.topk(gate_probs, self.top_k, dim=-1)
        top_k_gate_probs = top_k_gate_probs / top_k_gate_probs.sum(dim=-1, keepdim=True)
        
        # Initialize output
        out = torch.zeros_like(x_flat)
        
        # Process with each expert
        for expert_idx in range(self.num_experts):
            # Get indices where this expert is in top-k
            expert_mask = (top_k_indices == expert_idx).any(dim=-1)
            
            if expert_mask.any():
                # Get inputs for this expert
                expert_input = x_flat[expert_mask]
                
                # Process with expert
                expert_output = self.experts[expert_idx](expert_input)
                
                # Get gate weights for this expert
                weights = torch.where(
                    top_k_indices[expert_mask] == expert_idx,
                    top_k_gate_probs[expert_mask],
                    torch.zeros_like(top_k_gate_probs[expert_mask])
                ).sum(dim=-1, keepdim=True)
                
                # Add weighted expert output to final output
                out[expert_mask] += weights * expert_output
        
        # Reshape back to original dimensions
        out = out.reshape(batch_size, seq_len, self.d_model)
        out = self.dropout(out)
        return out

class GraphomerLayer(nn.Module):
    """Graphomer Layer combining graph conv and transformer with MoE"""
    def __init__(self, d_model: int, num_heads: int, d_ff: int, 
                 num_experts: int = 4, top_k: int = 2, dropout: float = 0.1):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.dropout = dropout
        
        # Graph convolution
        self.graph_conv = GraphConv(d_model, d_model)
        
        # Self-attention
        self.self_attn = nn.MultiheadAttention(d_model, num_heads, dropout=dropout)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        
        # MoE FFN
        self.moe = MoELayer(d_model, d_ff, num_experts, top_k, dropout)
        
    def forward(self, x: Tensor, adj: Tensor, key_padding_mask: Optional[Tensor] = None) -> Tensor:
        """
        Args:
            x: Input tensor [batch_size, num_nodes, d_model]
            adj: Adjacency matrix [batch_size, num_nodes, num_nodes]
            key_padding_mask: Mask for padding [batch_size, num_nodes]
        Returns:
            Output tensor [batch_size, num_nodes, d_model]
        """
        # Graph convolution
        graph_out = self.graph_conv(x, adj)
        x = x + graph_out
        
        # Self-attention
        attn_input = x.transpose(0, 1)  # [num_nodes, batch_size, d_model] for MHA
        attn_output, _ = self.self_attn(
            attn_input, attn_input, attn_input,
            key_padding_mask=key_padding_mask
        )
        attn_output = attn_output.transpose(0, 1)  # [batch_size, num_nodes, d_model]
        x = self.norm1(x + attn_output)
        
        # MoE FFN
        moe_output = self.moe(x)
        x = self.norm2(x + moe_output)
        
        return x

class Graphomer(nn.Module):
    """Graphomer Model with MoE Support"""
    def __init__(self, num_layers: int, d_model: int, num_heads: int, d_ff: int,
                 num_experts: int = 4, top_k: int = 2, dropout: float = 0.1):
        super().__init__()
        self.layers = nn.ModuleList([
            GraphomerLayer(d_model, num_heads, d_ff, num_experts, top_k, dropout)
            for _ in range(num_layers)
        ])
        
    def forward(self, x: Tensor, adj: Tensor, key_padding_mask: Optional[Tensor] = None) -> Tensor:
        """
        Args:
            x: Input tensor [batch_size, num_nodes, d_model]
            adj: Adjacency matrix [batch_size, num_nodes, num_nodes]
            key_padding_mask: Mask for padding [batch_size, num_nodes]
        Returns:
            Output tensor [batch_size, num_nodes, d_model]
        """
        for layer in self.layers:
            x = layer(x, adj, key_padding_mask)
        return x


# Example usage
batch_size = 4
num_nodes = 32
d_model = 128
num_heads = 8
d_ff = 512
num_layers = 6
num_experts = 8
top_k = 2

# Create random input and adjacency matrix
x = torch.randn(batch_size, num_nodes, d_model)
adj = torch.rand(batch_size, num_nodes, num_nodes)
adj = (adj > 0.5).float()  # Binarize adjacency matrix

# Create model
model = Graphomer(
    num_layers=num_layers,
    d_model=d_model,
    num_heads=num_heads,
    d_ff=d_ff,
    num_experts=num_experts,
    top_k=top_k
)

# Forward pass
output = model(x, adj)
print(output.shape)  # Should be [4, 32, 128]