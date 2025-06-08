import torch
import torch.nn as nn
import torch.nn.functional as F

class PatchEmbedding(nn.Module):
    """
    Converts an image into a sequence of flattened patches and projects them.
    """
    def __init__(self, img_size=224, patch_size=16, in_channels=3, embed_dim=768):
        super().__init__()
        self.img_size = img_size
        self.patch_size = patch_size
        self.n_patches = (img_size // patch_size) ** 2

        # Efficiently create patches and project them using a single convolution
        # kernel_size and stride are patch_size
        self.proj = nn.Conv2d(
            in_channels,
            embed_dim,
            kernel_size=patch_size,
            stride=patch_size
        )

    def forward(self, x):
        # x: (batch_size, in_channels, img_size, img_size)
        x = self.proj(x)  # (batch_size, embed_dim, n_patches_h, n_patches_w)
        x = x.flatten(2)  # (batch_size, embed_dim, n_patches)
        x = x.transpose(1, 2)  # (batch_size, n_patches, embed_dim)
        return x

class Attention(nn.Module):
    """
    Multi-Head Self-Attention block.
    Using PyTorch's built-in nn.MultiheadAttention for simplicity.
    """
    def __init__(self, embed_dim, num_heads, dropout_prob=0.0):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        assert self.head_dim * num_heads == embed_dim, "embed_dim must be divisible by num_heads"

        self.multihead_attn = nn.MultiheadAttention(embed_dim, num_heads, dropout=dropout_prob, batch_first=True)

    def forward(self, x):
        # x: (batch_size, seq_len, embed_dim)
        attn_output, _ = self.multihead_attn(x, x, x) # query, key, value are the same for self-attention
        # attn_output: (batch_size, seq_len, embed_dim)
        return attn_output

class MLP(nn.Module):
    """
    Feed-Forward Network (MLP block) for the Transformer Encoder.
    """
    def __init__(self, embed_dim, mlp_size, dropout_prob=0.1):
        super().__init__()
        self.fc1 = nn.Linear(embed_dim, mlp_size)
        self.act = nn.GELU() # GELU is commonly used in Transformers
        self.fc2 = nn.Linear(mlp_size, embed_dim)
        self.dropout = nn.Dropout(dropout_prob)

    def forward(self, x):
        x = self.fc1(x)
        x = self.act(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.dropout(x)
        return x

class TransformerEncoderBlock(nn.Module):
    """
    A single block of the Transformer Encoder.
    """
    def __init__(self, embed_dim, num_heads, mlp_size, dropout_prob=0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(embed_dim)
        self.attn = Attention(embed_dim, num_heads, dropout_prob=dropout_prob)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.mlp = MLP(embed_dim, mlp_size, dropout_prob=dropout_prob)
        self.dropout = nn.Dropout(dropout_prob) # Often an additional dropout is applied after sum

    def forward(self, x):
        # x: (batch_size, seq_len, embed_dim)
        # Attention sub-layer
        h = x
        x = self.norm1(x)
        x = self.attn(x)
        x = self.dropout(x) # Dropout after attention
        x = x + h # Residual connection

        # MLP sub-layer
        h = x
        x = self.norm2(x)
        x = self.mlp(x)
        # No dropout here in original ViT for this residual sum, but some impls add it
        x = x + h # Residual connection
        return x

class VisionTransformer(nn.Module):
    """
    Vision Transformer (ViT) model.
    """
    def __init__(self,
                 img_size=224,
                 patch_size=16,
                 in_channels=3,
                 num_classes=1000,
                 embed_dim=768,
                 depth=12, # Number of Transformer encoder blocks
                 num_heads=12,
                 mlp_size=3072, # Hidden dimension of MLP
                 dropout_prob=0.1,
                 emb_dropout_prob=0.1):
        super().__init__()

        self.patch_embedding = PatchEmbedding(img_size, patch_size, in_channels, embed_dim)
        num_patches = self.patch_embedding.n_patches

        # Learnable CLS token
        self.cls_token = nn.Parameter(torch.zeros(1, 1, embed_dim)) # (1, 1, embed_dim)

        # Learnable Positional embeddings
        # +1 for the CLS token
        self.pos_embedding = nn.Parameter(torch.zeros(1, num_patches + 1, embed_dim))
        self.pos_dropout = nn.Dropout(emb_dropout_prob)

        # Transformer Encoder
        self.encoder_blocks = nn.ModuleList([
            TransformerEncoderBlock(embed_dim, num_heads, mlp_size, dropout_prob)
            for _ in range(depth)
        ])

        # MLP Head for classification
        self.norm = nn.LayerNorm(embed_dim) # Final layer norm before MLP head
        self.mlp_head = nn.Linear(embed_dim, num_classes)

        # Initialize weights (common practice)
        self._initialize_weights()

    def _initialize_weights(self):
        # Initialize positional embedding and CLS token
        nn.init.normal_(self.pos_embedding, std=0.02)
        nn.init.normal_(self.cls_token, std=0.02)

        # Initialize nn.Linear and nn.Conv2d
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.LayerNorm):
                nn.init.constant_(m.bias, 0)
                nn.init.constant_(m.weight, 1.0)
            elif isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu') # or 'fan_in'
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)


    def forward(self, x):
        # x: (batch_size, in_channels, img_size, img_size)
        batch_size = x.shape[0]

        # 1. Patch Embedding
        x = self.patch_embedding(x)  # (batch_size, num_patches, embed_dim)

        # 2. Prepend CLS token
        # Expand cls_token to match batch size
        cls_tokens = self.cls_token.expand(batch_size, -1, -1) # (batch_size, 1, embed_dim)
        x = torch.cat((cls_tokens, x), dim=1) # (batch_size, num_patches + 1, embed_dim)

        # 3. Add Positional Embeddings
        x = x + self.pos_embedding # Broadcasting applies here
        x = self.pos_dropout(x)

        # 4. Pass through Transformer Encoder blocks
        for block in self.encoder_blocks:
            x = block(x)
            # x: (batch_size, num_patches + 1, embed_dim)

        # 5. MLP Head (Classification)
        # Use the output of the CLS token for classification
        cls_token_final_representation = self.norm(x[:, 0]) # (batch_size, embed_dim)
        logits = self.mlp_head(cls_token_final_representation) # (batch_size, num_classes)

        return logits

# --- Example Usage ---
if __name__ == '__main__':
    # Configuration (can be adjusted)
    img_s = 224          # Image size (e.g., 224x224)
    patch_s = 16         # Patch size (e.g., 16x16)
    in_chans = 3         # Number of input channels (e.g., 3 for RGB)
    n_classes = 10       # Number of output classes (e.g., for CIFAR-10 or a custom dataset)

    # Smaller model for quick testing
    emb_dim = 192        # Embedding dimension (e.g., ViT-Small uses 384, ViT-Base 768)
    n_layers = 6         # Number of Transformer layers (e.g., ViT-Small 8, ViT-Base 12)
    n_heads = 6          # Number of attention heads (e.g., ViT-Small 6, ViT-Base 12)
    mlp_hidden_dim = emb_dim * 4 # Standard MLP hidden dim relative to embed_dim

    # Create a dummy input tensor
    # batch_size = 4
    dummy_img = torch.randn(4, in_chans, img_s, img_s)

    # Instantiate the Vision Transformer model
    vit_model = VisionTransformer(
        img_size=img_s,
        patch_size=patch_s,
        in_channels=in_chans,
        num_classes=n_classes,
        embed_dim=emb_dim,
        depth=n_layers,
        num_heads=n_heads,
        mlp_size=mlp_hidden_dim,
        dropout_prob=0.1,
        emb_dropout_prob=0.1
    )

    # Perform a forward pass
    print(f"Input shape: {dummy_img.shape}")
    output_logits = vit_model(dummy_img)
    print(f"Output logits shape: {output_logits.shape}") # Should be (batch_size, num_classes)

    # Count parameters
    total_params = sum(p.numel() for p in vit_model.parameters() if p.requires_grad)
    print(f"Total trainable parameters: {total_params / 1e6:.2f} M")

    # Test with different patch size (ensure image size is divisible by patch size)
    img_s_2 = 32
    patch_s_2 = 8
    vit_model_2 = VisionTransformer(
        img_size=img_s_2,
        patch_size=patch_s_2,
        in_channels=in_chans,
        num_classes=n_classes,
        embed_dim=emb_dim,
        depth=n_layers,
        num_heads=n_heads,
        mlp_size=mlp_hidden_dim
    )
    dummy_img_2 = torch.randn(2, in_chans, img_s_2, img_s_2)
    print(f"\nInput shape 2: {dummy_img_2.shape}")
    output_logits_2 = vit_model_2(dummy_img_2)
    print(f"Output logits shape 2: {output_logits_2.shape}")
    total_params_2 = sum(p.numel() for p in vit_model_2.parameters() if p.requires_grad)
    print(f"Total trainable parameters (model 2): {total_params_2 / 1e6:.2f} M")