import torch
import torch.nn as nn

class LSTMCell(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(LSTMCell, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size

        # Parameters for input gate
        self.W_ix = nn.Linear(input_size, hidden_size)
        self.W_ih = nn.Linear(hidden_size, hidden_size)
        self.b_i = nn.Parameter(torch.zeros(hidden_size))

        # Parameters for forget gate
        self.W_fx = nn.Linear(input_size, hidden_size)
        self.W_fh = nn.Linear(hidden_size, hidden_size)
        self.b_f = nn.Parameter(torch.zeros(hidden_size))

        # Parameters for cell gate
        self.W_cx = nn.Linear(input_size, hidden_size)
        self.W_ch = nn.Linear(hidden_size, hidden_size)
        self.b_c = nn.Parameter(torch.zeros(hidden_size))

        # Parameters for output gate
        self.W_ox = nn.Linear(input_size, hidden_size)
        self.W_oh = nn.Linear(hidden_size, hidden_size)
        self.b_o = nn.Parameter(torch.zeros(hidden_size))

    def forward(self, input, hidden):
        h_prev, c_prev = hidden

        # Compute input gate
        i_t = torch.sigmoid(self.W_ix(input) + self.W_ih(h_prev) + self.b_i)

        # Compute forget gate
        f_t = torch.sigmoid(self.W_fx(input) + self.W_fh(h_prev) + self.b_f)

        # Compute cell gate
        g_t = torch.tanh(self.W_cx(input) + self.W_ch(h_prev) + self.b_c)

        # Compute new cell state
        c_t = f_t * c_prev + i_t * g_t

        # Compute output gate
        o_t = torch.sigmoid(self.W_ox(input) + self.W_oh(h_prev) + self.b_o)

        # Compute new hidden state
        h_t = o_t * torch.tanh(c_t)

        return h_t, c_t

class BasicLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(BasicLSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        # LSTM layers
        self.lstm = nn.ModuleList()
        self.lstm.append(LSTMCell(input_size, hidden_size))
        for _ in range(num_layers - 1):
            self.lstm.append(LSTMCell(hidden_size, hidden_size))

    def forward(self, input_data, hidden_state):
        h_0, c_0 = hidden_state
        outputs = []
        for i, input_t in enumerate(input_data):
            h_t, c_t = [], []
            for layer in range(self.num_layers):
                if i == 0:
                    h_prev, c_prev = h_0[layer], c_0[layer]
                else:
                    h_prev, c_prev = h_t[layer], c_t[layer]
                h_i, c_i = self.lstm[layer](input_t, (h_prev, c_prev))
                h_t.append(h_i)
                c_t.append(c_i)
                input_t = h_i
            outputs.append(input_t)
        return torch.stack(outputs), (torch.stack(h_t), torch.stack(c_t))

# Define input size, hidden size, and number of layers
input_size = 10
hidden_size = 20
num_layers = 2

# Create an instance of BasicLSTM
lstm = BasicLSTM(input_size, hidden_size, num_layers)

# Create some dummy input data and initial hidden state
input_data = torch.randn(5, 3, input_size)  # Sequence length 5, batch size 3
h_0 = torch.zeros(num_layers, 3, hidden_size)  # Initial hidden state
c_0 = torch.zeros(num_layers, 3, hidden_size)  # Initial cell state
hidden_state = (h_0, c_0)

# Forward pass through the LSTM
output, (h_n, c_n) = lstm(input_data, hidden_state)

# Print the output shape and final hidden and cell states
print("Output shape:", output.shape)
print("Final hidden state shape:", h_n.shape)
print("Final cell state shape:", c_n.shape)