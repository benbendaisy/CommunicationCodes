import numpy as np

class MultiHeadAttention:
    def __init__(self, d_model, num_heads):
        self.d_model = d_model
        self.num_heads = num_heads
        self.depth = d_model // num_heads

        # Initialize weight matrices for Q, K, and V
        self.Wq = np.random.randn(d_model, d_model)
        self.Wk = np.random.randn(d_model, d_model)
        self.Wv = np.random.randn(d_model, d_model)

        # Initialize weight matrix for output
        self.Wo = np.random.randn(d_model, d_model)

    def split_heads(self, x, batch_size):
        x = np.reshape(x, (batch_size, -1, self.num_heads, self.depth))
        return np.transpose(x, (0, 2, 1, 3))

    def scaled_dot_product_attention(self, Q, K, V):
        dk = np.sqrt(self.depth)
        QK = np.matmul(Q, K.T) / dk
        attention_weights = np.softmax(QK, axis=-1)
        output = np.matmul(attention_weights, V)
        return output

    def forward(self, Q, K, V):
        batch_size = Q.shape[0]

        # Linear transformations
        Q = np.matmul(Q, self.Wq)
        K = np.matmul(K, self.Wk)
        V = np.matmul(V, self.Wv)

        # Split heads
        Q = self.split_heads(Q, batch_size)
        K = self.split_heads(K, batch_size)
        V = self.split_heads(V, batch_size)

        # Scaled dot-product attention
        attention_output = self.scaled_dot_product_attention(Q, K, V)

        # Concatenate heads
        attention_output = np.transpose(attention_output, (0, 2, 1, 3))
        attention_output = np.reshape(attention_output, (batch_size, -1, self.d_model))

        # Linear transformation for output
        output = np.matmul(attention_output, self.Wo)

        return output


class PositionwiseFeedforward:
    def __init__(self, d_model, d_ff):
        self.W1 = np.random.randn(d_model, d_ff)
        self.W2 = np.random.randn(d_ff, d_model)

    def forward(self, x):
        x = np.matmul(x, self.W1)
        x = np.maximum(0, x)
        x = np.matmul(x, self.W2)
        return x


class TransformerLayer:
    def __init__(self, d_model, num_heads, d_ff):
        self.multi_head_attention = MultiHeadAttention(d_model, num_heads)
        self.positionwise_feedforward = PositionwiseFeedforward(d_model, d_ff)

    def forward(self, x):
        attention_output = self.multi_head_attention.forward(x, x, x)
        output = self.positionwise_feedforward.forward(attention_output)
        return output


class Transformer:
    def __init__(self, num_layers, d_model, num_heads, d_ff):
        self.layers = [TransformerLayer(d_model, num_heads, d_ff) for _ in range(num_layers)]

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x


# Example usage
num_layers = 2
d_model = 128
num_heads = 8
d_ff = 512

transformer = Transformer(num_layers, d_model, num_heads, d_ff)
input_data = np.random.randn(1, 10, d_model)  # Input sequence length 10, input features d_model
output = transformer.forward(input_data)
print("Output shape:", output.shape)