import numpy as np

class Conv2D:
    def __init__(self, input_channels, num_filters, kernel_size, stride=1, padding=0):
        self.input_channels = input_channels
        self.num_filters = num_filters
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

        self.filters = np.random.randn(num_filters, input_channels, kernel_size, kernel_size) * 0.01
        self.biases = np.zeros((num_filters, 1))

    def forward(self, inputs):
        self.inputs = inputs
        self.batch_size, self.input_channels, self.input_height, self.input_width = inputs.shape

        self.output_height = (self.input_height - self.kernel_size + 2 * self.padding) // self.stride + 1
        self.output_width = (self.input_width - self.kernel_size + 2 * self.padding) // self.stride + 1

        self.outputs = np.zeros((self.batch_size, self.num_filters, self.output_height, self.output_width))

        for b in range(self.batch_size):
            for f in range(self.num_filters):
                for h in range(self.output_height):
                    for w in range(self.output_width):
                        vert_start = h * self.stride
                        vert_end = vert_start + self.kernel_size
                        horiz_start = w * self.stride
                        horiz_end = horiz_start + self.kernel_size

                        receptive_field = inputs[b, :, vert_start:vert_end, horiz_start:horiz_end]
                        self.outputs[b, f, h, w] = np.sum(receptive_field * self.filters[f]) + self.biases[f]

        return self.outputs

class MaxPooling2D:
    def __init__(self, pool_size, stride):
        self.pool_size = pool_size
        self.stride = stride

    def forward(self, inputs):
        self.inputs = inputs
        self.batch_size, self.num_channels, self.input_height, self.input_width = inputs.shape

        self.output_height = (self.input_height - self.pool_size) // self.stride + 1
        self.output_width = (self.input_width - self.pool_size) // self.stride + 1

        self.outputs = np.zeros((self.batch_size, self.num_channels, self.output_height, self.output_width))

        for b in range(self.batch_size):
            for c in range(self.num_channels):
                for h in range(self.output_height):
                    for w in range(self.output_width):
                        vert_start = h * self.stride
                        vert_end = vert_start + self.pool_size
                        horiz_start = w * self.stride
                        horiz_end = horiz_start + self.pool_size

                        receptive_field = inputs[b, c, vert_start:vert_end, horiz_start:horiz_end]
                        self.outputs[b, c, h, w] = np.max(receptive_field)

        return self.outputs

class Flatten:
    def forward(self, inputs):
        self.batch_size = inputs.shape[0]
        self.outputs = inputs.reshape(self.batch_size, -1)
        return self.outputs

class Dense:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))

    def forward(self, inputs):
        self.inputs = inputs
        self.outputs = np.dot(inputs, self.weights) + self.biases
        return self.outputs

class ReLU:
    def forward(self, inputs):
        return np.maximum(0, inputs)

class Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        return probabilities

class CNN:
    def __init__(self):
        self.layers = []

    def add(self, layer):
        self.layers.append(layer)

    def forward(self, inputs):
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs

# Example usage
cnn = CNN()
cnn.add(Conv2D(input_channels=1, num_filters=3, kernel_size=3, stride=1, padding=1))
cnn.add(ReLU())
cnn.add(MaxPooling2D(pool_size=2, stride=2))
cnn.add(Flatten())
cnn.add(Dense(input_size=14*14*3, output_size=10))
cnn.add(Softmax())

# Example input data
input_data = np.random.randn(1, 28, 28)
input_data = input_data[np.newaxis, :, :, :]

# Forward pass
output = cnn.forward(input_data)
print("Output shape:", output.shape)