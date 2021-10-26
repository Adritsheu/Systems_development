#!/usr/bin/python3

#Part 1E
import Regression as reg
from sklearn import datasets
from sklearn.model_selection import train_test_split
#import regression classes

dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

alpha = 0.1
model1 = reg.LinearRegression()
model2 = reg.RidgeRegression()

model1.set_params(alpha = 0.1)
model2.set_params(alpha = 0.1)
models = [model1, model2]

r2_list = []

for model in models:
    model.fit(X_train, y_train);
    r2 = model.score(X_test, y_test)
    r2_list.append(r2)
    
    
print(r2_list)

max_r2 = max(r2_list)
index = r2_list.index(max_r2)
best_model = models[index]
print(best_model.get_params())
