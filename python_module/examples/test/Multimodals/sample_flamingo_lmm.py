import torch
import torch.nn as nn
from transformers import CLIPModel, CLIPProcessor, GPT2LMHeadModel, GPT2Tokenizer
from PIL import Image
from transformers import CLIPProcessor

# Cross-attention block for vision-text fusion
class CrossAttentionBlock(nn.Module):
    def __init__(self, dim, num_heads):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim=dim, num_heads=num_heads, batch_first=True)
        self.norm = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, dim * 4),
            nn.GELU(),
            nn.Linear(dim * 4, dim)
        )

    def forward(self, x, visual_embeds, attention_mask=None):
        # x: (B, T, D), visual_embeds: (B, V, D)
        x_ = self.norm(x)
        vis_ = self.norm(visual_embeds)
        attn_out, _ = self.attn(x_, vis_, vis_)  # Query is text, keys/values are vision
        x = x + attn_out
        x = x + self.mlp(self.norm(x))
        return x

# Simplified Flamingo Model
class FlamingoMini(nn.Module):
    def __init__(self, vision_model_name='openai/clip-vit-base-patch32', 
                 language_model_name='gpt2', num_cross_layers=2):
        super().__init__()

        # Frozen vision encoder (CLIP)
        self.vision_encoder = CLIPModel.from_pretrained(vision_model_name).vision_model
        for p in self.vision_encoder.parameters():
            p.requires_grad = False

        # Frozen language model (GPT2)
        self.language_model = GPT2LMHeadModel.from_pretrained(language_model_name)
        for p in self.language_model.parameters():
            p.requires_grad = False

        self.cross_attention_blocks = nn.ModuleList([
            CrossAttentionBlock(dim=self.language_model.config.n_embd,
                                num_heads=self.language_model.config.n_head)
            for _ in range(num_cross_layers)
        ])

        self.tokenizer = GPT2Tokenizer.from_pretrained(language_model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def forward(self, images, input_ids, attention_mask):
        # Get visual embeddings from vision encoder
        vision_outputs = self.vision_encoder(images).last_hidden_state  # (B, V, D)

        # Get language model hidden states
        lm_inputs = self.language_model.transformer.wte(input_ids)  # (B, T, D)

        # Interleave cross-attention blocks
        hidden = lm_inputs
        for block in self.cross_attention_blocks:
            hidden = block(hidden, vision_outputs)

        # Use modified embeddings for LM head
        lm_logits = self.language_model.lm_head(hidden)  # (B, T, Vocab)
        return lm_logits

# --- Main Execution ---
if __name__ == '__main__':
    # Dummy image and text input
    image = Image.open("/Users/bendaisyarthurannie/Downloads/vanilla.png").convert("RGB")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    inputs = processor(images=image, return_tensors="pt")

    # Tokenize text
    text = ["A picture of vanila flower"]
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    text_inputs = tokenizer(text, return_tensors="pt", padding=True)

    # Forward pass
    model = FlamingoMini()
    logits = model(images=inputs['pixel_values'], 
                input_ids=text_inputs['input_ids'], 
                attention_mask=text_inputs['attention_mask'])
    
    print(f"logits are: {logits}")
