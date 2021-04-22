import matplotlib.pyplot as plt
import math
x = []
p = 0.3
n = 100
def ncr(n,r):
    return math.factorial(n)/math.factorial(n-r)/math.factorial(r)
for i in range(n):
    x.append(ncr(n,i)*p**i*(1-p)**(n-i))
plt.figure("Binmonal p =  "+str(p))
plt.title('pmf')
plt.plot(range(n), x, label = 'P(H) = '+str(p))
plt.legend()
c = [] 
for i in range(len(x)):
    c.append(sum(x[:i+1]))
plt.figure("Binmonal p =  "+str(p))
plt.plot(c, label = 'P(H) = '+str(p))
plt.legend()
plt.show()
