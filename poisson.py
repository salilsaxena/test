import numpy as np 
import matplotlib.pyplot as plt
from math import *
X = []
l = [1,4,10, 20]
r = [float(i) for i in range(100)]
for i in l: 
    X.append([])
    for j in range(0,len(r)):
        X[-1].append(i**j * e**(-i) / factorial(j))

plt.figure(1)
for i in range(len(X)):
#    plt.figure(i)
    plt.scatter(r,X[i])
    plt.plot(r,X[i],label = 'lamda = '+str(l[i]))
plt.legend()
C = [] 
for  i in range(len(l)): 
    C.append([])
    for j in range(len(X[i])):
        C[-1].append(sum(X[i][:j+1]))
plt.figure(2)
for i in range(len(C)):
    plt.scatter(r,C[i])
    plt.plot(r,C[i], label = 'lamda = '+str(l[i]))
plt.legend()
plt.show()
def mean(x):
    s = 0 
    for i in x: 
        s+=i
    return s/len(x)
def var(x):
    s = 0 
    m = mean(x)
    for i in x: 
        s+=(i-m)**2
    return s/len(x)
