#!/usr/bin/python3
import numpy as np

def layer_func(shape,actv):
    def layer(inputs, weights, bias):
        if shape[0] != inputs.shape[0]:
            raise ValueError(f"shape mismatch on inputs")
        if shape[1] != weights.shape[1]:
            raise ValueError(f"Shape mismatch on weights")
        if shape[1] != bias.shape[0]:
            raise ValueError(f"Shape mismatch on bias")
        output = actv(weights.T @ inputs + bias)
        return output
    return layer
    
t = np.random.uniform(0.0, 1.0, 100).reshape(-1,1) # input to the network

shape1 = (100,20)
shape2 = (20,10)

layer1 = layer_func(shape1, np.tanh) # Define layer 1
layer2 = layer_func(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.random.rand(100,20)
w2 = np.random.rand(20,10)
b1 = np.random.rand(20,1)
b2 = np.random.rand(10,1)

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer
    
print(f"h1 is {h1}")
print(f"h2is {h2}")
