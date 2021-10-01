# Pair Programming #5

import numpy as np

class Layer():
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        self.weights = np.random.rand(*shape)
        self.bias = np.random.rand(shape[1],1)
        
    def forward(self,inputs):
        outputs = self.actv(self.weights.T @ inputs + self.bias)
        return outputs
        
    def __str__(self):
        return(f"Here is shape of our self: {self.shape}")
    
    def __repr__(self):
        return(f"Here Layer object of: {id(self)}")
    
    def __add__(self,layer):
        if self.shape == layer.shape:
            self.weights += layer.weights
        else:
            raise ValueError(f"Shape mismatch on weights")
        return self.weights


shape1 = (100,20)
shape2 = (20,10)
actv = np.tanh

inputs = np.random.rand(100,1)

# Run through the network
layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)

h1 = layer1.forward(inputs)
h2 = layer2.forward(h1)

print(Layer(shape1,actv))
print(repr(layer2))

print(f"here is the sum of layer1 with itself {layer1+layer1}")

    
print(f"h1 is {h1}")
print(f"h2 is {h2}")


        
    
