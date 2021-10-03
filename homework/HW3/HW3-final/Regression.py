
#!/usr/bin/python3

# Problem 2a: Create a module
import numpy as np
import matplotlib.pyplot as plt


 

class Regression():

    def __init__(self):
        # your code
        self.params = {}
       
    def get_params(self):
        # your code
        return self.params

    def set_params(self, **kwargs):
        # your code
        #Manually set parameters of the linear model. The method should accept variable keyword arguments (**kwargs)
        #containing model parameters. In this problem, it will be used to set the regularization coefficient α
        #in the Ridge Regression model.
        #raise NotImplementedError
        pass

    def fit(self, X, y):
        # your code
        raise NotImplementedError
        
    def predict(self, X):
        # your code
        raise NotImplementedError

    def score(self, X, y):
        # your code
        ypred = self.predict(X)
        ymean = y.mean()
        

        SST = np.sum((y - ymean)**2)
        SSE = np.sum((y - ypred)**2)
        R2 = 1 - (SSE/SST)
        return R2
    
# Part 2C

class LinearRegression(Regression):
    
    def _init__(self):
        super().__init__()
    
    def fit(self, X, y):
        #need to add bias to X append the ones
        bias = np.ones((X.shape[0],1))  #columns of ones length of X
        X = np.hstack((bias, X))
        
        #FIT
        betaLR = np.linalg.pinv(X.T @ X) @ (X.T @ y)
        interceptLR = betaLR[0]
        coeffLR = betaLR[1:]
        self.params["coeff"] = coeffLR
        self.params["intercept"] = interceptLR
               
    
    def predict(self, X):
        # your code
        y_pred = X @ self.params["coeff"] + self.params["intercept"]
        return y_pred

#Part 2D
        
class RidgeRegression(LinearRegression):
    
    def _init__(self):
        super().__init__()
    
    def set_params(self, **kwargs):
        for value in kwargs.values():
            self.alpha = value


    def fit(self, X, y):
        #need to add bias to X append the ones
        bias = np.ones((X.shape[0],1))  #columns of ones length of X
        X = np.hstack((bias, X))
        
        I = np.identity(X.shape[1])
        Gamma = self.alpha * I
        betaRR = np.linalg.pinv(X.T @ X + Gamma.T @ Gamma) @ (X.T @ y)
        interceptRR = betaRR[0]
        coeffRR = betaRR[1:]
        self.params["coeff"] = coeffRR
        self.params["intercept"] = interceptRR
        

    def predict(self, X):
    # your code
        y_pred = X @ self.params["coeff"] + self.params["intercept"]
        return y_pred
    

