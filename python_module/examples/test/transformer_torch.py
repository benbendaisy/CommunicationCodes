import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        assert d_model % self.num_heads == 0
        self.depth = d_model // self.num_heads

        self.Wq = nn.Linear(d_model, d_model)
        self.Wk = nn.Linear(d_model, d_model)
        self.Wv = nn.Linear(d_model, d_model)
        self.Wo = nn.Linear(d_model, d_model)

    def split_heads(self, x, batch_size):
        x = x.view(batch_size, -1, self.num_heads, self.depth)
        return x.permute(0, 2, 1, 3)

    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)

        # Linear transformations
        Q = self.Wq(query)
        K = self.Wk(key)
        V = self.Wv(value)

        # Split heads
        Q = self.split_heads(Q, batch_size)
        K = self.split_heads(K, batch_size)
        V = self.split_heads(V, batch_size)

        # Scaled dot-product attention
        scores = torch.matmul(Q, K.permute(0, 1, 3, 2)) / torch.sqrt(torch.tensor(self.depth, dtype=torch.float32))
        if mask is not None:
            scores += mask.unsqueeze(1)
        attention_weights = F.softmax(scores, dim=-1)
        attention_output = torch.matmul(attention_weights, V)

        # Concatenate heads
        attention_output = attention_output.permute(0, 2, 1, 3).contiguous().view(batch_size, -1, self.d_model)

        # Linear transformation for output
        output = self.Wo(attention_output)

        return output, attention_weights


class PositionwiseFeedforward(nn.Module):
    def __init__(self, d_model, d_ff):
        super(PositionwiseFeedforward, self).__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x


class TransformerEncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff):
        super(TransformerEncoderLayer, self).__init__()
        self.multi_head_attention = MultiHeadAttention(d_model, num_heads)
        self.feedforward = PositionwiseFeedforward(d_model, d_ff)

    def forward(self, x, mask=None):
        attention_output, _ = self.multi_head_attention(x, x, x, mask)
        output = self.feedforward(attention_output)
        return output


class TransformerEncoder(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, d_ff):
        super(TransformerEncoder, self).__init__()
        self.layers = nn.ModuleList([TransformerEncoderLayer(d_model, num_heads, d_ff) for _ in range(num_layers)])

    def forward(self, x, mask=None):
        for layer in self.layers:
            x = layer(x, mask)
        return x


class TransformerDecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff):
        super(TransformerDecoderLayer, self).__init__()
        self.masked_multi_head_attention = MultiHeadAttention(d_model, num_heads)
        self.multi_head_attention = MultiHeadAttention(d_model, num_heads)
        self.feedforward = PositionwiseFeedforward(d_model, d_ff)

    def forward(self, x, encoder_output, src_mask=None, tgt_mask=None):
        # Self-attention
        attention_output, _ = self.masked_multi_head_attention(x, x, x, tgt_mask)
        x = x + attention_output
        # Encoder-decoder attention
        attention_output, _ = self.multi_head_attention(x, encoder_output, encoder_output, src_mask)
        x = x + attention_output
        # Feedforward
        output = self.feedforward(x)
        return output


class TransformerDecoder(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, d_ff):
        super(TransformerDecoder, self).__init__()
        self.layers = nn.ModuleList([TransformerDecoderLayer(d_model, num_heads, d_ff) for _ in range(num_layers)])

    def forward(self, x, encoder_output, src_mask=None, tgt_mask=None):
        for layer in self.layers:
            x = layer(x, encoder_output, src_mask, tgt_mask)
        return x


class Transformer(nn.Module):
    def __init__(self, num_encoder_layers, num_decoder_layers, d_model, num_heads, d_ff, input_vocab_size, output_vocab_size):
        super(Transformer, self).__init__()
        self.encoder = TransformerEncoder(num_encoder_layers, d_model, num_heads, d_ff)
        self.decoder = TransformerDecoder(num_decoder_layers, d_model, num_heads, d_ff)
        self.linear = nn.Linear(d_model, output_vocab_size)

    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        encoder_output = self.encoder(src, src_mask)
        decoder_output = self.decoder(tgt, encoder_output, src_mask, tgt_mask)
        output = self.linear(decoder_output)
        return output


# Example usage
num_encoder_layers = 6
num_decoder_layers = 6
d_model = 512
num_heads = 8
d_ff = 2048
input_vocab_size = 10000
output_vocab_size = 10000
seq_len = 10
batch_size = 32

# Create Transformer model
transformer_model = Transformer(num_encoder_layers, num_decoder_layers, d_model, num_heads, d_ff, input_vocab_size, output_vocab_size)

# Generate random input sequence
src_seq = torch.randn(batch_size, seq_len, d_model)
tgt_seq = torch.randn(batch_size, seq_len, d_model)

# Create masks for source and target sequences
src_mask = torch.ones(batch_size, seq_len)
tgt_mask = torch.ones(batch_size, seq_len)

# Forward pass
output_seq = transformer_model(src_seq, tgt_seq, src_mask, tgt_mask)

# Print output shape
print("Output sequence shape:", output_seq.shape)