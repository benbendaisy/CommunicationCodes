import torch
import torch.nn as nn

class SimpleRNNCell(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(SimpleRNNCell, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size

        # Initialize weight matrices
        self.Wxh = nn.Linear(input_size, hidden_size)  # Weight matrix for input
        self.Whh = nn.Linear(hidden_size, hidden_size)  # Weight matrix for hidden state
        self.bh = nn.Parameter(torch.zeros(hidden_size))  # Bias vector for hidden state
        self.tanh = nn.Tanh()

    def forward(self, x, h):
        # Perform RNN step
        h = self.tanh(self.Wxh(x) + self.Whh(h) + self.bh)
        return h

class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn_cell = SimpleRNNCell(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, input_data, hidden_state):
        seq_length = input_data.size(0)
        output = torch.zeros(seq_length, self.hidden_size)
        for i in range(seq_length):
            hidden_state = self.rnn_cell(input_data[i], hidden_state)
            output[i] = hidden_state
        output = self.fc(output)
        output = self.softmax(output)
        return output

# Define input size, hidden size, and output size
input_size = 10
hidden_size = 20
output_size = 5

# Create an instance of SimpleRNN
rnn = SimpleRNN(input_size, hidden_size, output_size)

# Create some dummy input data and initial hidden state
input_data = torch.randn(3, input_size)  # Sequence length 3
hidden_state = torch.zeros(1, hidden_size)  # Initial hidden state

# Forward pass through the RNN
output = rnn(input_data, hidden_state)

# Print the output
print("Output shape:", output.shape)
print("Output:")
print(output)