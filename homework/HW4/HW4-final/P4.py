#!/usr/bin/python3

## Problem 4 : A Toy AD implementation
class AutoDiffToy():

    def __init__(self,val, der = 1):
        self.val = val
        self.der = der
        
    def __mul__(self, other):
        try:
            value = self.val * other.val  # must do the value
            der = self.der * other.val + self.val * other.der # chain rule
        except AttributeError:
            value = self.val * other # when you don't store the values
            der = self.der * other
        return AutoDiffToy(value,der)   # need to return the attributes so that the instance is updated
    
    def __rmul__(self, other):
        return self.__mul__(other) #to get the other order
    
    def __add__(self, other):
        try:
            value = self.val + other.val
            der = self.der + other.der
        except AttributeError:
            value = self.val + other
            der = self.der + 0
        return AutoDiffToy(value,der)

    
    def __radd__(self, other):
        return self.__add__(other)  #to get the other order
        
    
    
    def __str__(self):
        s = f"Value: {self.val}"
        if hasattr(self, "der"):
            s += f", Derivative of x: {self.der}"
        return s

    

if __name__ == "__main__":
    a = 2.0  # Value to evaluate at
    x = AutoDiffToy(a)
    alpha = 3.0
    beta = 5.0
    
    f1 = alpha * x + beta
    f2 = x * alpha + beta
    f3 = beta + alpha * x
    f4 = beta + x * alpha
    
    
    f_list = [f1, f2, f3, f4]
    formula = ["f = alpha * x + beta","f = x * alpha + beta","f = beta + alpha * x","f = beta + x * alpha"]
    for index, values in enumerate(f_list):
        print(formula[index])
        print(f"{values} \n")
        
