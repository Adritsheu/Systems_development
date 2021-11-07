#!/usr/bin/python3

# Motivating Automatic differentiation
# Test the Finite Difference to True Derivative
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

def numerical_diff(f,h):
    
    def closure(x):
        f_prime = (f(x+h) - f(x))/h
        return f_prime
    
    return closure


def f_real(x):
    return 1/x

h = [10**-1,10**-7, 10**-15]
x = np.array(np.linspace(0.2,0.4,10))

#f_list, freal_list = [],[]

f_ar = []


for i in h:
    sub_f = []
    #print(f"f_ar {f_ar}")
    
    for j in x:
       # print(index)
       # print(i)
        func = numerical_diff(np.log, i)(j)
        sub_f.append(func)
        #print(sub_f)
        
    f_ar.append(sub_f)
   
    
f_ar = np.array([f_ar])
f_ar1 = f_ar[:,0].reshape(-1,1)
f_ar2 = f_ar[:,1].reshape(-1,1)
f_ar3 = f_ar[:,2].reshape(-1,1)

freal =([f_real(xx) for xx in x])


print("Q-a: Which value of h most closely approximates the true derivative? What happens for values \
of h that are too small? What happens for values of h that are too large?\n")

print("Answer to Q-a: The value of h = 1 x 10^-7 is closest to the true derivative.\
 For values of h that are too small the derivative, gets to be inconsistent and you \
can see that with the purple line, which can be due to truncation errors. With values of h that are too large, the\
derivative value is not similar to the actual derivative, which can come from rounding errors.\n")

print("Q-b: How does automatic differentiation address these problems? \n")
print("Answer to Q-b: To compute a derivative, it can take a lot computing power to solve for the entire curve \
for a function. Automatic differentiation just looks at one value of x to derive the derivative for \
the entire function, and can reduce our computing. AD uses the chain rule to evaluate complex derivatives,\
 and makes our evaluated derivative more precise. As seen with the graph, choosing the optimal h size is important for getting the correct derivative. \n")

plt.figure()
plt.plot(x,freal,'g--',label = 'True Derivative' )
plt.plot(x,f_ar1,'r--',label = r'Finite Difference function for h = $1 x 10^{-1}$')
plt.plot(x,f_ar2,'y--',label = r'Finite Difference function for h = $1 x 10^{-7}$')
plt.plot(x,f_ar3,'m--',label = r'Finite Difference function for h = $1 x 10^{-15}$')
plt.title("Finite Differences for 3 h values and the True derivative")
plt.xlabel("Values of h")
plt.ylabel("Values for the derivative")
plt.legend()
plt.savefig("P1_fig.png", dpi = 300, bbox_inches = 'tight')
plt.show()
