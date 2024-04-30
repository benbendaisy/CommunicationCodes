import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class DummyRNN(nn.Module):

    def __init__(self, input_features, output_features):
        super(DummyRNN, self).__init__()
        self.W = nn.Linear(input_features, output_features)
        self.U = nn.Linear(output_features, output_features)
        self.b = nn.Parameter(torch.randn(output_features))
        self.state = torch.zeros(output_features)

    def forward(self, input_data, concatenate):
        memory = []
        for input_t in input_data:
            output_t = torch.tanh(self.W(input_t) + self.U(self.state) + self.b)
            memory.append(output_t)
            self.state = output_t
        if concatenate:
            result = torch.cat(memory, axis=0)
        else:
            result = memory
        return result

time_steps = 100
input_features = 32
output_features = 64

model = DummyRNN(input_features, output_features)
dummy_input = torch.randn(time_steps, input_features)
print(len(model.forward(dummy_input, concatenate=True)))

# class MyRNN(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(MyRNN, self).__init__()
#         self.hidden_size = hidden_size
#         self.in2hidden = nn.Linear(input_size + hidden_size, hidden_size)
#         self.in2output = nn.Linear(input_size + hidden_size, output_size)
    
#     def forward(self, x, hidden_state):
#         combined = torch.cat((x, hidden_state), 1)
#         hidden = torch.sigmoid(self.in2hidden(combined))
#         output = self.in2output(combined)
#         return output, hidden
    
#     def init_hidden(self):
#         return nn.init.kaiming_uniform_(torch.empty(1, self.hidden_size))

# class RNN(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(RNN, self).__init__()

#         self.hidden_size = hidden_size

#         self.i2h = nn.Linear(input_size, hidden_size)
#         self.h2h = nn.Linear(hidden_size, hidden_size)
#         self.h2o = nn.Linear(hidden_size, output_size)
#         self.softmax = nn.LogSoftmax(dim=1)

#     def forward(self, input, hidden):
#         hidden = F.tanh(self.i2h(input) + self.h2h(hidden))
#         output = self.h2o(hidden)
#         output = self.softmax(output)
#         return output, hidden

#     def initHidden(self):
#         return torch.zeros(1, self.hidden_size)
