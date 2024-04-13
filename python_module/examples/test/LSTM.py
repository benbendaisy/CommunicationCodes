import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.Wf = np.random.randn(hidden_size, input_size + hidden_size)  # Forget gate weights
        self.bf = np.zeros((hidden_size, 1))  # Forget gate bias

        self.Wi = np.random.randn(hidden_size, input_size + hidden_size)  # Input gate weights
        self.bi = np.zeros((hidden_size, 1))  # Input gate bias

        self.Wo = np.random.randn(hidden_size, input_size + hidden_size)  # Output gate weights
        self.bo = np.zeros((hidden_size, 1))  # Output gate bias

        self.Wc = np.random.randn(hidden_size, input_size + hidden_size)  # Cell state weights
        self.bc = np.zeros((hidden_size, 1))  # Cell state bias

        # Output layer weights
        self.Wy = np.random.randn(output_size, hidden_size)
        self.by = np.zeros((output_size, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def tanh(self, x):
        return np.tanh(x)

    def forward(self, x, prev_h, prev_c):
        concat = np.concatenate((prev_h, x), axis=0)

        # Forget gate
        ft = self.sigmoid(np.dot(self.Wf, concat) + self.bf)

        # Input gate
        it = self.sigmoid(np.dot(self.Wi, concat) + self.bi)

        # Output gate
        ot = self.sigmoid(np.dot(self.Wo, concat) + self.bo)

        # Candidate cell state (unactivated)
        c_hat = self.tanh(np.dot(self.Wc, concat) + self.bc)

        # Current cell state
        c = ft * prev_c + it * c_hat

        # Hidden state
        h = ot * self.tanh(c)

        # Output
        output = np.dot(self.Wy, h) + self.by
        return output, h, c

    def backward(self, x, prev_h, prev_c, dh_next, dc_next, lr):
        concat = np.concatenate((prev_h, x), axis=0)

        # Backprop into output layer
        dWy = np.dot(dh_next, prev_h.T)
        dby = dh_next

        # Backprop into hidden state
        dh = np.dot(self.Wy.T, dh_next) + dh_next

        # Backprop through the tanh
        d_c = dc_next + (1 - np.tanh(prev_c)**2) * dh * prev_c

        # Backprop into output gate
        dot = d_c * self.tanh(prev_c)
        dot = dot * (ot * (1 - ot))

        # Backprop into input gate
        dit = d_c * c_hat
        dit = dit * (it * (1 - it))

        # Backprop into forget gate
        dft = d_c * prev_c
        dft = dft * (ft * (1 - ft))

        # Backprop into candidate cell state
        dc_hat = d_c * it
        dc_hat = dc_hat * (1 - c_hat**2)

        # Concatenate derivatives
        dconcat = np.vstack([dft, dit, dot, dc_hat])

        # Backprop into Wf, Wi, Wo, Wc
        dWf = np.dot(dft, concat.T)
        dWi = np.dot(dit, concat.T)
        dWo = np.dot(dot, concat.T)
        dWc = np.dot(dc_hat, concat.T)

        # Derivatives for biases
        dbf = np.sum(dft, axis=1, keepdims=True)
        dbi = np.sum(dit, axis=1, keepdims=True)
        dbo = np.sum(dot, axis=1, keepdims=True)
        dbc = np.sum(dc_hat, axis=1, keepdims=True)

        # Derivatives for input x
        dx = np.dot(self.Wf[:, :self.input_size].T, dft) + np.dot(self.Wi[:, :self.input_size].T, dit) + \
             np.dot(self.Wo[:, :self.input_size].T, dot) + np.dot(self.Wc[:, :self.input_size].T, dc_hat)

        # Update weights and biases
        self.Wf -= lr * dWf
        self.Wi -= lr * dWi
        self.Wo -= lr * dWo
        self.Wc -= lr * dWc
        self.Wy -= lr * dWy
        self.bf -= lr * dbf
        self.bi -= lr * dbi
        self.bo -= lr * dbo
        self.bc -= lr * dbc
        self.by -= lr * dby

        return dx[:self.input_size], h_prev, c_prev

# Example usage
input_size = 3
hidden_size = 5
output_size = 2
lstm = LSTM(input_size, hidden_size, output_size)

# Dummy input data
x = np.random.randn(input_size, 1)
prev_h = np.random.randn(hidden_size, 1)
prev_c = np.random.randn(hidden_size, 1)
dh_next = np.random.randn(output_size, 1)
dc_next = np.random.randn(hidden_size, 1)

# Forward pass
output, h, c = lstm.forward(x, prev_h, prev_c)
print("Output:", output)

# Backward pass
dx, dh_prev, dc_prev = lstm.backward(x, prev_h, prev_c, dh_next, dc_next, lr=0.01)
print("dx:", dx)