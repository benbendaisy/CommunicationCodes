import torch
import torch.nn as nn
from torch.nn import functional as F

class Head(nn.Module):
    """One head of self-attention"""
    def __init__(self, head_size, n_embd, decoder=None):
        super().__init__()
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))
        self.dropout = nn.Dropout(dropout)
        self.decoder = decoder

    def forward(self, x):
        B, T, C = x.shape
        # print(f"x'shape = {x.shape}")
        k = self.key(x)  # (B,T,C)
        q = self.query(x)  # (B,T,C)
        # compute attention scores ("affinities")
        wei = q @ k.transpose(-2, -1) * C ** -0.5  # (B, T, C) @ (B, C, T) -> (B, T, T) with scaler C**-0.5
        if self.decoder is not None:
            wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf'))  # (B, T, T) masked head so that transformer can only see all tokens before current tokens
        wei = F.softmax(wei, dim=-1)  # (B, T, T)
        wei = self.dropout(wei)
        # perform the weighted aggregation of the values
        v = self.value(x)  # (B,T,C)
        out = wei @ v  # (B, T, T) @ (B, T, C) -> (B, T, C)
        return out


class MultiHeadAttention(nn.Module):
    """Multiple heads of self-attention in parallel"""

    def __init__(self, num_heads, head_size, n_embd, n_out, decoder=None):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size, n_embd, decoder) for _ in range(num_heads)])
        self.proj = nn.Linear(n_embd, n_out)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        out = self.proj(out)
        out = self.dropout(out)
        return out


class FeedFoward(nn.Module):
    """ a simple linear layer followed by a non-linearity """
    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        return self.net(x)


class EncoderBlock(nn.Module):
    """Encoder block for the Transformer"""

    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size, n_embd, n_embd)
        self.ffwd = FeedFoward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x):
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x


class DecoderBlock(nn.Module):
    """Decoder block for the Transformer"""

    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa_decoder = MultiHeadAttention(n_head, head_size, n_embd, n_embd, True)
        self.sa_encoder_decoder = MultiHeadAttention(n_head, 2 * head_size, 2 * n_embd, n_embd, None)
        self.ffwd = FeedFoward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(2 * n_embd)
        self.ln3 = nn.LayerNorm(n_embd)

    def forward(self, x, encoder_output):
        x = x + self.sa_decoder(self.ln1(x))
        # print(f"x's shape = {x.shape}")
        # print(f"encoder_output's shape = {encoder_output.shape}")
        # print(f"cat's shape = {self.ln2(torch.cat([x, encoder_output], dim=-1)).shape}")
        x = x + self.sa_encoder_decoder(self.ln2(torch.cat([x, encoder_output], dim=-1)))
        x = x + self.ffwd(self.ln3(x))
        return x


class Transformer(nn.Module):
    """Transformer model with encoder and decoder blocks"""

    def __init__(self, vocab_size, n_embd, n_head, n_layer):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.encoder_blocks = nn.ModuleList([EncoderBlock(n_embd, n_head) for _ in range(n_layer)])
        self.decoder_blocks = nn.ModuleList([DecoderBlock(n_embd, n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, src_idx, tgt_idx):
        B, T_src = src_idx.shape
        B, T_tgt = tgt_idx.shape

        src_tok_emb = self.token_embedding_table(src_idx)
        tgt_tok_emb = self.token_embedding_table(tgt_idx)

        src_pos_emb = self.position_embedding_table(torch.arange(T_src, device=device))
        tgt_pos_emb = self.position_embedding_table(torch.arange(T_tgt, device=device))

        src_x = src_tok_emb + src_pos_emb
        tgt_x = tgt_tok_emb + tgt_pos_emb

        encoder_output = src_x
        for encoder_block in self.encoder_blocks:
            encoder_output = encoder_block(encoder_output)

        decoder_output = tgt_x
        for decoder_block in self.decoder_blocks:
            decoder_output = decoder_block(decoder_output, encoder_output)

        decoder_output = self.ln_f(decoder_output)

        logits = self.lm_head(decoder_output)

        loss = F.cross_entropy(logits.view(-1, logits.size(-1)), tgt_idx.view(-1))

        return logits, loss

# Define hyperparameters
vocab_size = 1000
n_embd = 256
n_head = 8
n_layer = 6
dropout = 0.1
block_size = 1
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Instantiate the Transformer model
model = Transformer(vocab_size, n_embd, n_head, n_layer)

# Define optimizer and loss function
optimizer = torch.optim.AdamW(model.parameters(), lr=0.001)
# criterion = nn.CrossEntropyLoss()

# Define training loop
def train_model(model, optimizer, src_input, tgt_input):
    model.train()
    optimizer.zero_grad(set_to_none=True)
    # src_mask = (src_input != 0).unsqueeze(1).unsqueeze(2)
    # tgt_mask = (tgt_input != 0).unsqueeze(1).unsqueeze(2)

    logits, loss = model(src_input, tgt_input)
    loss.backward()
    optimizer.step()
    return logits, loss

# Define inference function
# def generate_sequence(model, src_input, max_length=100):
#     model.eval()
#     with torch.no_grad():
#         B, T_src = src_input.shape
#         tgt_input = torch.zeros((B, 1), dtype=torch.long, device=src_input.device)  # Start with an empty target sequence
#         for i in range(max_length):
#             logits = model(src_input, tgt_input)
#             predicted_token = logits[:, -1, :].argmax(dim=-1, keepdim=True)
#             tgt_input = torch.cat([tgt_input, predicted_token], dim=1)  # Append the predicted token to the target sequence
#             if torch.all(predicted_token == 3):  # Stop if all predicted tokens are EOS (end-of-sequence) tokens
#                 break
#     return tgt_input[:, 1:] 

# Sample training and inference
# src_input = torch.randint(1, vocab_size, (8, n_embd)).to(device)  # Example source input
# tgt_input = torch.randint(1, vocab_size, (8, n_embd)).to(device)  # Example target input
# logits, loss = train_model(model, optimizer, src_input, tgt_input)
# print(logits.shape)

# Example usage:
# src_input = torch.randint(1, vocab_size, (8, n_embd))  # Example source input
# generated_sequences = generate_sequence(model, src_input)
# print(generated_sequences)
# inference_result = infer(model, src_input)
# print("Inference result:", inference_result)