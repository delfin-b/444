import numpy as np
import matplotlib.pyplot as plt

t = np.arange(start=0, stop=101, step=1) # defining t as a numpy array starts from 0 and ends  100

v0 = 5
g = 10

y = []

for i in t:
	
	a = v0*i + (1/2)*g*i**2 
	y = np.append(y,a)

plt.xlabel('t') 
plt.ylabel('y')
plt.title('y versus t graph')
fit1 = np.polyfit(t, y, 1)  # polynomially fitting
plt.plot(t, np.polyval(fit1, t), color='b', linestyle='-', label='fitted data') # ploting the fitted data
plt.plot(t, y, marker='.', color='r', label="not fitted", linestyle='-') # ploting the non-fitted data
plt.legend(loc='best') # put a "legend" to the best location on the graph

plt.show()  