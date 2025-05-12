# --- MLP (Multi-Layer Perceptron) Class ---

class MLP(nn.Module):
    """
    A simple Multi-Layer Perceptron with one hidden layer.

    This module is used within the Transformer block for feed-forward processing.
    It expands the input embedding size, applies a ReLU activation, and then projects it back
    to the original embedding size.
    """
    def __init__(self, n_embed):
        super().__init__()
        self.hidden = nn.Linear(n_embed, 4 * n_embed)  # Linear layer to expand embedding size
        self.relu = nn.ReLU()                        # ReLU activation function
        self.proj = nn.Linear(4 * n_embed, n_embed)  # Linear layer to project back to original size

    def forward(self, x):
        """
        Forward pass through the MLP.

        Args:
            x (torch.Tensor): Input tensor of shape (B, T, C), where B is batch size,
                              T is sequence length, and C is embedding size.

        Returns:
            torch.Tensor: Output tensor of the same shape as the input.
        """
        x = self.forward_embedding(x)
        x = self.project_embedding(x)
        return x

    def forward_embedding(self, x):
        """
        Applies the hidden linear layer followed by ReLU activation.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output after the hidden layer and ReLU.
        """
        x = self.relu(self.hidden(x))
        return x

    def project_embedding(self, x):
        """
        Applies the projection linear layer.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output after the projection layer.
        """
        x = self.proj(x)
        return x

# --- Attention Head Class ---

class Head(nn.Module):
    """
    A single attention head.

    This module calculates attention scores and applies them to the values.
    It includes key, query, and value projections, and uses causal masking
    to prevent attending to future tokens.
    """
    def __init__(self, head_size, n_embed, context_length, drop_out=0.3):
        super().__init__()
        self.key = nn.Linear(n_embed, head_size, bias=False)   # Key projection
        self.query = nn.Linear(n_embed, head_size, bias=False) # Query projection
        self.value = nn.Linear(n_embed, head_size, bias=False) # Value projection
        # Lower triangular matrix for causal masking
        self.register_buffer('tril', torch.tril(torch.ones(context_length, context_length)))
        self.fc_out = nn.Linear(head_size, head_size)
        self.drop_out = nn.Linear(drop_out)

    def forward(self, x):
        """
        Forward pass through the attention head.

        Args:
            x (torch.Tensor): Input tensor of shape (B, T, C).

        Returns:
            torch.Tensor: Output tensor after applying attention.
        """
        _, T, C = x.shape
        k = self.key(x)     # (B, T, head_size)
        q = self.query(x)   # (B, T, head_size)
        scale_factor = 1 / math.sqrt(C)
        # Calculate attention weights: (B, T, head_size) @ (B, head_size, T) -> (B, T, T)
        attn_weights = q @ k.transpose(-2, -1) * scale_factor
        # Apply causal masking
        attn_weights = attn_weights.masked_fill(self.tril[:T, :T] == 0, float('-inf'))
        attn_weights = F.softmax(attn_weights, dim=-1)
        attn_weights = self.drop_out(attn_weights)
        v = self.value(x)   # (B, T, head_size)
        # Apply attention weights to values
        out = attn_weights @ v # (B, T, T) @ (B, T, head_size) -> (B, T, head_size)

        return self.fc_out(out)


# --- Multi-Head Attention Class ---

class MultiHeadAttention(nn.Module):
    """
    Multi-Head Attention module.

    This module combines multiple attention heads in parallel. The outputs of each head
    are concatenated to form the final output.
    """
    def __init__(self, n_head, n_embed, context_length):
        super().__init__()
        self.heads = nn.ModuleList([Head(n_embed // n_head, n_embed, context_length) for _ in range(n_head)])

    def forward(self, x):
        """
        Forward pass through the multi-head attention.

        Args:
            x (torch.Tensor): Input tensor of shape (B, T, C).

        Returns:
            torch.Tensor: Output tensor after concatenating the outputs of all heads.
        """
        # Concatenate the output of each head along the last dimension (C)
        x = torch.cat([h(x) for h in self.heads], dim=-1)
        return x

# --- Transformer Block Class ---

class Block(nn.Module):
    """
    A single Transformer block.

    This block consists of a multi-head attention layer followed by an MLP,
    with layer normalization and residual connections.
    """
    def __init__(self, n_head, n_embed, context_length):
        super().__init__()
        self.ln1 = nn.LayerNorm(n_embed)
        self.attn = MultiHeadAttention(n_head, n_embed, context_length)
        self.ln2 = nn.LayerNorm(n_embed)
        self.mlp = MLP(n_embed)

    def forward(self, x):
        """
        Forward pass through the Transformer block.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor after the block.
        """
        # Apply multi-head attention with residual connection
        x = x + self.attn(self.ln1(x))
        # Apply MLP with residual connection
        x = x + self.mlp(self.ln2(x))
        return x

    def forward_embedding(self, x):
        """
        Forward pass focusing on the embedding and attention parts.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            tuple: A tuple containing the output after MLP embedding and the residual.
        """
        res = x + self.attn(self.ln1(x))
        x = self.mlp.forward_embedding(self.ln2(res))
        return x, res

# --- Transformer Model Class ---

class Transformer(nn.Module):
    """
    The main Transformer model.

    This class combines token and position embeddings with a sequence of Transformer blocks
    and a final linear layer for language modeling.
    """
    def __init__(self, n_head, n_embed, context_length, vocab_size, N_BLOCKS):
        super().__init__()
        self.context_length = context_length
        self.N_BLOCKS = N_BLOCKS
        self.token_embed = nn.Embedding(vocab_size, n_embed)
        self.position_embed = nn.Embedding(context_length, n_embed)
        self.attn_blocks = nn.ModuleList([Block(n_head, n_embed, context_length) for _ in range(N_BLOCKS)])
        self.layer_norm = nn.LayerNorm(n_embed)
        self.lm_head = nn.Linear(n_embed, vocab_size)
        self.register_buffer('pos_idxs', torch.arange(context_length))

    def _pre_attn_pass(self, idx):
        """
        Combines token and position embeddings.

        Args:
            idx (torch.Tensor): Input token indices.

        Returns:
            torch.Tensor: Sum of token and position embeddings.
        """
        _, T = idx.shape
        tok_embedding = self.token_embed(idx)
        pos_embedding = self.position_embed(self.pos_idxs[:T])
        return tok_embedding + pos_embedding

    def forward(self, idx, targets=None):
        """
        Forward pass through the Transformer.

        Args:
            idx (torch.Tensor): Input token indices.
            targets (torch.Tensor, optional): Target token indices for loss calculation. Defaults to None.

        Returns:
            tuple: Logits and loss (if targets are provided).
        """
        x = self._pre_attn_pass(idx)
        for block in self.attn_blocks:
            x = block(x)
        x = self.layer_norm(x)
        logits = self.lm_head(x)
        loss = None
        if targets is not None:
            B, T, C = logits.shape
            flat_logits = logits.view(B * T, C)
            targets = targets.view(B * T).long()
            loss = F.cross_entropy(flat_logits, targets)
        return logits, loss

    def forward_embedding(self, idx):
        """
        Forward pass focusing on the embedding and attention blocks.

        Args:
            idx (torch.Tensor): Input token indices.

        Returns:
            tuple: Output after attention blocks and the residual.
        """
        x = self._pre_attn_pass(idx)
        residual = x
        for block in self.attn_blocks:
            x, residual = block.forward_embedding(x)
        return x, residual

    def generate(self, idx, max_new_tokens):
        """
        Generates new tokens given a starting sequence.

        Args:
            idx (torch.Tensor): Initial sequence of token indices.
            max_new_tokens (int): Number of tokens to generate.

        Returns:
            torch.Tensor: The extended sequence of tokens.
        """
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -self.context_length:]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, idx_next), dim=1)
        return idx