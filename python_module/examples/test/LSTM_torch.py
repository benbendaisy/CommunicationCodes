import torch
import torch.nn as nn

class LSTMCell(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(LSTMCell, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size

        # Input gate weights
        self.W_ii = nn.Parameter(torch.Tensor(input_size, hidden_size))
        self.W_hi = nn.Parameter(torch.Tensor(hidden_size, hidden_size))
        self.b_i = nn.Parameter(torch.Tensor(hidden_size))

        # Forget gate weights
        self.W_if = nn.Parameter(torch.Tensor(input_size, hidden_size))
        self.W_hf = nn.Parameter(torch.Tensor(hidden_size, hidden_size))
        self.b_f = nn.Parameter(torch.Tensor(hidden_size))

        # Cell gate weights
        self.W_ig = nn.Parameter(torch.Tensor(input_size, hidden_size))
        self.W_hg = nn.Parameter(torch.Tensor(hidden_size, hidden_size))
        self.b_g = nn.Parameter(torch.Tensor(hidden_size))

        # Output gate weights
        self.W_io = nn.Parameter(torch.Tensor(input_size, hidden_size))
        self.W_ho = nn.Parameter(torch.Tensor(hidden_size, hidden_size))
        self.b_o = nn.Parameter(torch.Tensor(hidden_size))

        self.init_weights()

    def init_weights(self):
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)

    def forward(self, x, prev_hidden_state, prev_cell_state):
        # Input gate
        i = torch.sigmoid(torch.mm(x, self.W_ii) + torch.mm(prev_hidden_state, self.W_hi) + self.b_i)
        # Forget gate
        f = torch.sigmoid(torch.mm(x, self.W_if) + torch.mm(prev_hidden_state, self.W_hf) + self.b_f)
        # Cell gate
        g = torch.tanh(torch.mm(x, self.W_ig) + torch.mm(prev_hidden_state, self.W_hg) + self.b_g)
        # Output gate
        o = torch.sigmoid(torch.mm(x, self.W_io) + torch.mm(prev_hidden_state, self.W_ho) + self.b_o)

        cell_state = f * prev_cell_state + i * g
        hidden_state = o * torch.tanh(cell_state)

        return hidden_state, cell_state

class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(LSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.lstm_cell = LSTMCell(input_size, hidden_size)

    def forward(self, input_seq):
        batch_size, seq_len, _ = input_seq.size()
        hidden_state = torch.zeros(batch_size, self.hidden_size)
        cell_state = torch.zeros(batch_size, self.hidden_size)
        output_seq = []

        for t in range(seq_len):
            hidden_state, cell_state = self.lstm_cell(input_seq[:, t, :], hidden_state, cell_state)
            output_seq.append(hidden_state.unsqueeze(1))

        output_seq = torch.cat(output_seq, dim=1)
        return output_seq, (hidden_state, cell_state)

# Example usage
input_size = 10
hidden_size = 32
seq_len = 5
batch_size = 2

# Create LSTM model
lstm_model = LSTM(input_size, hidden_size)

# Generate random input sequence
input_seq = torch.randn(batch_size, seq_len, input_size)

# Forward pass
output_seq, (final_hidden_state, final_cell_state) = lstm_model(input_seq)

# Print output shapes
print("Output sequence shape:", output_seq.shape)
print("Final hidden state shape:", final_hidden_state.shape)
print("Final cell state shape:", final_cell_state.shape)