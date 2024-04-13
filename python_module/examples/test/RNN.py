import numpy as np

class RNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.Wxh = np.random.randn(hidden_size, input_size) * 0.01  # Input to hidden
        self.Whh = np.random.randn(hidden_size, hidden_size) * 0.01  # Hidden to hidden
        self.Why = np.random.randn(output_size, hidden_size) * 0.01  # Hidden to output
        self.bh = np.zeros((hidden_size, 1))  # Hidden bias
        self.by = np.zeros((output_size, 1))  # Output bias

    def forward(self, inputs, h_prev):
        """
        Forward pass of the RNN.
        :param inputs: Input sequence of shape (input_size, sequence_length)
        :param h_prev: Previous hidden state of shape (hidden_size, 1)
        :return: Output sequence of shape (output_size, sequence_length), hidden state of shape (hidden_size, 1)
        """
        # Initialize outputs and hidden states
        outputs = []
        hs = []

        # Iterate over each time step
        for x in inputs.T:
            # Compute hidden state
            h = np.tanh(np.dot(self.Wxh, x) + np.dot(self.Whh, h_prev) + self.bh)

            # Compute output
            y = np.dot(self.Why, h) + self.by

            # Store output and hidden state
            outputs.append(y)
            hs.append(h)

            # Update previous hidden state
            h_prev = h

        # Convert outputs and hidden states to arrays
        outputs = np.array(outputs)
        hs = np.array(hs)

        return outputs, hs

    def backward(self, inputs, targets, hs):
        """
        Backward pass of the RNN.
        :param inputs: Input sequence of shape (input_size, sequence_length)
        :param targets: Target sequence of shape (output_size, sequence_length)
        :param hs: Hidden states of shape (hidden_size, sequence_length)
        :return: Gradients of weights and biases
        """
        # Initialize gradients
        dWxh, dWhh, dWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        dbh, dby = np.zeros_like(self.bh), np.zeros_like(self.by)
        dh_next = np.zeros_like(hs[0])

        # Backpropagate through time
        for t in reversed(range(len(inputs.T))):
            # Compute error at current time step
            dy = targets[:, t] - hs[t]

            # Compute gradients for output layer
            dWhy += np.dot(dy, hs[t].T)
            dby += dy

            # Compute error at current hidden state
            dh = np.dot(self.Why.T, dy) + dh_next

            # Compute gradients for hidden-to-hidden weights
            dh_raw = (1 - hs[t] ** 2) * dh
            dbh += dh_raw
            dWxh += np.dot(dh_raw, inputs[:, t].T)
            dWhh += np.dot(dh_raw, hs[t-1].T)

            # Update next hidden state gradient
            dh_next = np.dot(self.Whh.T, dh_raw)

        # Clip gradients to prevent exploding gradients
        for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
            np.clip(dparam, -5, 5, out=dparam)

        return dWxh, dWhh, dWhy, dbh, dby