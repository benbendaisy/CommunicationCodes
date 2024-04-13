import numpy as np

class Generator:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))

    def forward(self, z):
        return np.dot(z, self.weights) + self.biases

class Discriminator:
    def __init__(self, input_size):
        self.input_size = input_size
        self.weights = np.random.randn(input_size, 1) * 0.01
        self.biases = np.zeros((1, 1))

    def forward(self, x):
        return np.sigmoid(np.dot(x, self.weights) + self.biases)

class GAN:
    def __init__(self, latent_dim, data_dim, gen_hidden_dim, dis_hidden_dim):
        self.latent_dim = latent_dim
        self.data_dim = data_dim
        self.gen_hidden_dim = gen_hidden_dim
        self.dis_hidden_dim = dis_hidden_dim

        # Initialize generator and discriminator
        self.generator = Generator(latent_dim, data_dim)
        self.discriminator = Discriminator(data_dim)

    def train(self, real_data, num_epochs, batch_size, learning_rate):
        for epoch in range(num_epochs):
            # Train discriminator
            for _ in range(batch_size):
                # Sample real data
                real_batch = real_data[np.random.randint(0, len(real_data), batch_size)]

                # Generate fake data
                noise = np.random.randn(batch_size, self.latent_dim)
                fake_batch = self.generator.forward(noise)

                # Train discriminator
                real_predictions = self.discriminator.forward(real_batch)
                fake_predictions = self.discriminator.forward(fake_batch)

                d_loss = self.compute_discriminator_loss(real_predictions, fake_predictions)

                # Update discriminator parameters
                self.discriminator.weights -= learning_rate * d_loss
                self.discriminator.biases -= learning_rate * d_loss

            # Train generator
            noise = np.random.randn(batch_size, self.latent_dim)
            fake_batch = self.generator.forward(noise)

            # Train generator to fool discriminator
            fake_predictions = self.discriminator.forward(fake_batch)
            g_loss = self.compute_generator_loss(fake_predictions)

            # Update generator parameters
            self.generator.weights -= learning_rate * g_loss
            self.generator.biases -= learning_rate * g_loss

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Generator Loss: {g_loss}, Discriminator Loss: {d_loss}")

    def compute_discriminator_loss(self, real_predictions, fake_predictions):
        d_loss = -np.mean(np.log(real_predictions) + np.log(1 - fake_predictions))
        return d_loss

    def compute_generator_loss(self, fake_predictions):
        g_loss = -np.mean(np.log(fake_predictions))
        return g_loss

# Example usage
latent_dim = 100
data_dim = 784  # Assuming MNIST data with 28x28 images
gen_hidden_dim = 256
dis_hidden_dim = 256
num_epochs = 1000
batch_size = 64
learning_rate = 0.001

# Load real data (e.g., MNIST images)
real_data = np.random.randn(10000, data_dim)

# Initialize GAN
gan = GAN(latent_dim, data_dim, gen_hidden_dim, dis_hidden_dim)

# Train GAN
gan.train(real_data, num_epochs, batch_size, learning_rate)