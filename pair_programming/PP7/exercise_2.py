class Forward:
    def __init__(self,val):
        self.val = val
        
    def __pow__(self, other):
        temp = Forward(self.val ** other.val)
        temp.deriv = other.val * self.val **(other.val - 1)
        return temp
        
    def __str__(self):
        s = f"Value: {self.val}"
        if hasattr(self, "deriv"):
            s += f", Derivative of x: {self.deriv}"
        return s
    

if __name__ == "__main__":
    x = Forward(3)
    r = Forward(4)
    print(f"3^4 = {x**r}")
