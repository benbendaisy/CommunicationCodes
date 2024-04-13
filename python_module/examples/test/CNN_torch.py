import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Define convolutional layers
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        # Define max pooling layer
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        # Define fully connected layers
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)  # 10 classes for MNIST dataset

    def forward(self, x):
        # Apply first convolutional layer followed by ReLU activation and max pooling
        x = self.pool(F.relu(self.conv1(x)))
        # Apply second convolutional layer followed by ReLU activation and max pooling
        x = self.pool(F.relu(self.conv2(x)))
        # Flatten the tensor for fully connected layers
        x = x.view(-1, 32 * 7 * 7)
        # Apply fully connected layers with ReLU activation
        x = F.relu(self.fc1(x))
        # Apply final fully connected layer
        x = self.fc2(x)
        return x

# Instantiate the CNN model
model = SimpleCNN()

# Print the model architecture
print(model)