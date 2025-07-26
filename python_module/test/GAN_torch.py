import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Define the generator network
class Generator(nn.Module):
    def __init__(self, input_size, output_size):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, output_size),
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x)

# Define the discriminator network
class Discriminator(nn.Module):
    def __init__(self, input_size):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)

# Initialize the generator and discriminator
generator = Generator(input_size=100, output_size=784)
discriminator = Discriminator(input_size=784)

# Define the loss function and optimizer
criterion = nn.BCELoss()
optimizer_G = optim.Adam(generator.parameters(), lr=0.0002)
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002)

# Training loop
num_epochs = 100
batch_size = 64
for epoch in range(num_epochs):
    for i in range(0, len(data), batch_size):
        # Train discriminator with real data
        discriminator.zero_grad()
        real_images = data[i:i+batch_size]
        real_labels = torch.ones(batch_size, 1)
        real_outputs = discriminator(real_images)
        real_loss = criterion(real_outputs, real_labels)
        real_loss.backward()

        # Train discriminator with fake data
        z = torch.randn(batch_size, 100)
        fake_images = generator(z)
        fake_labels = torch.zeros(batch_size, 1)
        fake_outputs = discriminator(fake_images.detach())
        fake_loss = criterion(fake_outputs, fake_labels)
        fake_loss.backward()
        optimizer_D.step()

        # Train generator
        generator.zero_grad()
        fake_outputs = discriminator(fake_images)
        generator_loss = criterion(fake_outputs, real_labels)
        generator_loss.backward()
        optimizer_G.step()

        if i % 100 == 0:
            print(f"Epoch [{epoch}/{num_epochs}], Step [{i}/{len(data)}], "
                f"Generator Loss: {generator_loss.item()}, "
                f"Discriminator Loss: {real_loss.item() + fake_loss.item()}")

# Generate samples from the generator
z = torch.randn(10, 100)
fake_images = generator(z)