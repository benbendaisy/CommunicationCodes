import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class SimpleAttentionWithKVCache(nn.Module):
    def __init__(self, embed_dim, num_heads=1): # Simplified to num_heads=1 for clarity
        super().__init__()
        assert embed_dim % num_heads == 0, "embed_dim must be divisible by num_heads"
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        # Linear layers for Q, K, V
        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)

        self.drop_out = nn.Dropout(0.2)

        # Output projection
        self.out_proj = nn.Linear(embed_dim, embed_dim)

    def forward(self, x, past_kv=None, use_cache=False):
        """
        x: Input tensor of shape (batch_size, sequence_length, embed_dim)
        past_kv: A tuple (past_key, past_value) or None.
                 past_key shape: (batch_size, num_heads, past_sequence_length, head_dim)
                 past_value shape: (batch_size, num_heads, past_sequence_length, head_dim)
        use_cache: Boolean, if True, returns the updated K and V along with the output.
        """
        batch_size, seq_len, _ = x.shape

        # 1. Calculate Q, K, V for the current input tokens
        q = self.q_proj(x)  # (batch_size, seq_len, embed_dim)
        k = self.k_proj(x)  # (batch_size, seq_len, embed_dim)
        v = self.v_proj(x)  # (batch_size, seq_len, embed_dim)

        # Reshape for multi-head attention (or single head in our simplified case)
        # (batch_size, seq_len, num_heads, head_dim) -> (batch_size, num_heads, seq_len, head_dim)
        q = q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        k_current = k.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        v_current = v.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        # 2. KV Caching Logic
        present_kv = None
        if past_kv is not None:
            past_key, past_value = past_kv
            # Concatenate past K, V with current K, V
            # k shape: (batch_size, num_heads, total_seq_len, head_dim)
            # v shape: (batch_size, num_heads, total_seq_len, head_dim)
            k = torch.cat([past_key, k_current], dim=2)
            v = torch.cat([past_value, v_current], dim=2)
        else:
            # No past KV, so K and V are just the current ones
            k = k_current
            v = v_current

        if use_cache:
            present_kv = (k, v) # Store the updated K and V for the next step

        # 3. Scaled Dot-Product Attention
        # Q: (batch_size, num_heads, current_seq_len, head_dim)
        # K: (batch_size, num_heads, total_seq_len, head_dim)
        # V: (batch_size, num_heads, total_seq_len, head_dim)
        attn_scores = torch.matmul(q, k.transpose(-2, -1))  # (batch_size, num_heads, current_seq_len, total_seq_len)
        attn_scores = attn_scores / math.sqrt(self.head_dim)
        # Apply causal mask (important for autoregressive generation)
        # The mask ensures that a query at position i can only attend to keys at positions j <= i.
        # When using KV cache, `q` has seq_len=1 for generation, and `k` has `total_seq_len`.
        # The causal mask is implicitly handled if `q` only contains the current token's query
        # and `k` contains all keys up to the current token.
        # For a full sequence processing (seq_len > 1) without cache (e.g., training or processing a prompt):
        if seq_len > 1 and past_kv is None: # Only apply mask if processing a sequence from scratch
            mask = torch.triu(torch.ones_like(attn_scores), diagonal=1).bool()
            attn_scores = attn_scores.masked_fill(mask, float('-inf'))

        attn_probs = F.softmax(attn_scores, dim=-1)
        attn_probs = self.drop_out(attn_probs)
        attn_output = torch.matmul(attn_probs, v)  # (batch_size, num_heads, current_seq_len, head_dim)

        # 4. Concatenate heads and project
        attn_output = attn_output.transpose(1, 2).contiguous().view(batch_size, seq_len, self.embed_dim)
        output = self.out_proj(attn_output) # (batch_size, seq_len, embed_dim)

        if use_cache:
            return output, present_kv
        else:
            return output

# --- Example Usage ---
embed_dim = 64 # e.g., d_model
attention_layer = SimpleAttentionWithKVCache(embed_dim)

# --- Scenario 1: Processing a prompt (no cache initially, build cache) ---
print("--- Scenario 1: Processing a prompt ---")
batch_size = 1
prompt_len = 3
prompt_tokens_emb = torch.randn(batch_size, prompt_len, embed_dim) # Dummy embeddings

# Process prompt, no past_kv, ask to return cache
prompt_output, kv_cache_after_prompt = attention_layer(prompt_tokens_emb, past_kv=None, use_cache=True)
print("Prompt output shape:", prompt_output.shape)
print("K cache shape after prompt:", kv_cache_after_prompt[0].shape) # (batch, num_heads, prompt_len, head_dim)
print("V cache shape after prompt:", kv_cache_after_prompt[1].shape) # (batch, num_heads, prompt_len, head_dim)
print("\n")

# --- Scenario 2: Generating next token using the cache ---
print("--- Scenario 2: Generating 1st new token ---")
# Now, generate the (prompt_len + 1)-th token.
# The input `x` is just the embedding of the *last token* from the prompt_output or a new token.
# For simplicity, let's use a new dummy token embedding.
new_token_emb = torch.randn(batch_size, 2, embed_dim) # Input for the new token

# Pass the new token and the previously computed kv_cache
# `past_kv` is `kv_cache_after_prompt`
# `use_cache=True` to update the cache with this new token's K,V
next_token_output, kv_cache_after_token1 = attention_layer(new_token_emb, past_kv=kv_cache_after_prompt, use_cache=True)

print("Next token output shape:", next_token_output.shape) # Should be (batch_size, 1, embed_dim)
# The K,V cache should now have sequence length prompt_len + 1
print("K cache shape after 1st new token:", kv_cache_after_token1[0].shape)
print("V cache shape after 1st new token:", kv_cache_after_token1[1].shape)
print("\n")


# --- Scenario 3: Generating another token using the updated cache ---
print("--- Scenario 3: Generating 2nd new token ---")
another_new_token_emb = torch.randn(batch_size, 1, embed_dim)

# Pass the newest token and the updated cache from the previous step
next_token_output_2, kv_cache_after_token2 = attention_layer(another_new_token_emb, past_kv=kv_cache_after_token1, use_cache=True)

print("Next token output 2 shape:", next_token_output_2.shape)
# The K,V cache should now have sequence length prompt_len + 2
print("K cache shape after 2nd new token:", kv_cache_after_token2[0].shape)
print("V cache shape after 2nd new token:", kv_cache_after_token2[1].shape)
print("\n")

# --- Scenario 4: How it looks inside the attention for the 2nd new token ---
# For `next_token_output_2` generation:
# Q comes from `another_new_token_emb` (seq_len=1)
# K and V in `kv_cache_after_token1` have seq_len = prompt_len + 1
# K_current and V_current are from `another_new_token_emb` (seq_len=1)
# The `torch.cat` will make K and V for attention have seq_len = prompt_len + 2
# So Q (1 token) attends to K (prompt_len + 2 tokens)