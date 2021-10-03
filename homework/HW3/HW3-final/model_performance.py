#!/usr/bin/python3

#Part 2F
import Regression as reg
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

alpha = np.linspace(0.001,10,100)

dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

model1 = reg.LinearRegression()
model2 = reg.RidgeRegression()


r2_LR_m1 = []
r2_RR_m2 = []

models = [model1, model2]
for aval in alpha:
    model1.set_params(alpha = aval)
    model2.set_params(alpha = aval)
    
    model1.fit(X_train, y_train);
    model2.fit(X_train, y_train);
    
    r2_m1 = model1.score(X_test, y_test)
    r2_m2 = model2.score(X_test, y_test)
    r2_LR_m1.append(r2_m1)
    r2_RR_m2.append(r2_m2)
    
    
plt.figure(figsize = (6,6))
plt.plot(alpha, r2_LR_m1, 'g-', label = "Model 1: Linear Regression R2 scores")
plt.plot(alpha, r2_RR_m2, 'r-', label = "Model 2: Ridge Regression R2 scores")
plt.title("Comparision of Ridge and Linear Regression R2 scores")
plt.xlabel("Alpha values")
plt.ylabel("R2 scores")
plt.legend()
plt.draw()
plt.savefig("P2F.png", dpi = 300, bbox_inches = 'tight')

plt.show()
    
    

