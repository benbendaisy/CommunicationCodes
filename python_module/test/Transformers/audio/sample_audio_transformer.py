import torch
import torch.nn as nn
import math
import torchaudio


# Model Parameters
NUM_CLASSES = 10
D_MODEL = 128
N_HEAD = 8
NUM_ENCODER_LAYERS = 4
DIM_FEEDFORWARD = 512
N_MELS = 128 # Typical value for Mel Spectrograms


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding, self).__init__()
        # Create a long enough positional encoding matrix
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        
        # Calculate sine for even indices and cosine for odd indices
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        pe = pe.unsqueeze(0)
        
        # Register as a buffer so it's not a model parameter
        self.register_buffer('pe', pe)

    def forward(self, x):
        # Add positional encoding to the input
        # x shape: [seq_len, batch_size, d_model]
        x = x + self.pe[:, :x.size(1), :]
        return x
    

class TransformerEncoderLayer(nn.Module):
    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1):
        super(TransformerEncoderLayer, self).__init__()
        self.self_attn = nn.MultiheadAttention(d_model, nhead, dropout=dropout, batch_first=True)
        # Implementation of Feedforward model
        self.linear1 = nn.Linear(d_model, dim_feedforward)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(dim_feedforward, d_model)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

        self.activation = nn.ReLU()

    def forward(self, src):
        # Multi-head Self-Attention
        # The output of self_attn is (attn_output, attn_output_weights)
        attn_output, _ = self.self_attn(src, src, src)
        # Residual connection and Layer Normalization
        src = src + self.dropout1(attn_output)
        src = self.norm1(src)
        
        # Feed-Forward Network
        ff_output = self.linear2(self.dropout(self.activation(self.linear1(src))))
        # Residual connection and Layer Normalization
        src = src + self.dropout2(ff_output)
        src = self.norm2(src)
        
        return src


class AudioTransformer(nn.Module):
    def __init__(self, num_classes, d_model=128, nhead=8, num_encoder_layers=6, 
                 dim_feedforward=512, dropout=0.1, n_mels=80):
        super(AudioTransformer, self).__init__()
        
        self.d_model = d_model
        
        # 1. Audio Feature Extraction
        self.mel_spectrogram = torchaudio.transforms.MelSpectrogram(
            sample_rate=16000, 
            n_mels=n_mels
        )
        
        # 2. Input Projection
        # Project Mel spectrogram features to the model dimension
        self.input_proj = nn.Linear(n_mels, d_model)
        
        # 3. Positional Encoding
        # Note: We need to adjust positional encoding for batch_first=True format
        self.pos_encoder = PositionalEncoding(d_model)

        # 4. Transformer Encoder Stack
        encoder_layers = [TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout) 
                          for _ in range(num_encoder_layers)]
        self.transformer_encoder = nn.Sequential(*encoder_layers)
        
        # 5. Classification Head
        self.classifier = nn.Linear(d_model, num_classes)

    def forward(self, src):
        # 1. Feature Extraction
        # src shape: [batch_size, num_samples]
        mel_out = self.mel_spectrogram(src)
        # mel_out shape: [batch_size, n_mels, time_steps]
        
        # Reshape for transformer: [batch_size, time_steps, n_mels]
        mel_out = mel_out.permute(0, 2, 1)
        
        # 2. Input Projection
        # embedded shape: [batch_size, time_steps, d_model]
        embedded = self.input_proj(mel_out)
        
        # 3. Add Positional Encoding
        # The positional encoding class expects [seq_len, batch_size, d_model]
        # so we transpose, add encoding, and transpose back.
        embedded = embedded.permute(1, 0, 2)
        pos_encoded = self.pos_encoder(embedded)
        pos_encoded = pos_encoded.permute(1, 0, 2)
        
        # 4. Pass through Transformer Encoder
        # encoder_out shape: [batch_size, time_steps, d_model]
        encoder_out = self.transformer_encoder(pos_encoded)
        
        # 5. Pooling and Classification
        # We use mean pooling over the time dimension
        pooled_out = encoder_out.mean(dim=1)
        
        # Final classification
        logits = self.classifier(pooled_out)
        return logits
    

def main():
    # Instantiate the model
    model = AudioTransformer(
        num_classes=NUM_CLASSES,
        d_model=D_MODEL,
        nhead=N_HEAD,
        num_encoder_layers=NUM_ENCODER_LAYERS,
        dim_feedforward=DIM_FEEDFORWARD,
        n_mels=N_MELS
    )

    print(f"Model created with {sum(p.numel() for p in model.parameters()):,} trainable parameters.")

    # Create dummy input data
    BATCH_SIZE = 4
    # Assume 3 seconds of audio at 16kHz
    AUDIO_SAMPLES = 16000 * 3 
    dummy_waveform = torch.randn(BATCH_SIZE, AUDIO_SAMPLES)

    # Get model output
    logits = model(dummy_waveform)

    # Output shape should be [batch_size, num_classes]
    print("Input shape:", dummy_waveform.shape)
    print("Output logits shape:", logits.shape)
    # Example output:
    # Model created with 1,712,010 trainable parameters.
    # Input shape: torch.Size([4, 48000])
    # Output logits shape: torch.Size([4, 10])


if __name__ == "__main__":
    main()