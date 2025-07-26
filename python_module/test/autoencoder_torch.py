import torch
import torch.nn as nn
import torch.nn.functional as F

class Autoencoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Linear(input_size, hidden_size)
        self.decoder = nn.Linear(hidden_size, input_size)

    def forward(self, x):
        # Encode the input data
        encoded = F.relu(self.encoder(x))
        # Decode the encoded data
        decoded = torch.sigmoid(self.decoder(encoded))
        return decoded

# Example usage
input_size = 784  # Size of MNIST images (28x28)
hidden_size = 64  # Size of the hidden layer in the autoencoder

# Instantiate the autoencoder model
model = Autoencoder(input_size, hidden_size)

# Print the model architecture
print(model)