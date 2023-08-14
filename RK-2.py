
# python 3

import numpy as np
import math
import matplotlib.pyplot as plt

#DE func
def func(u,x):
	return x**2*math.exp(-(u+1))

#initials

#runge kutta 2nd order
def RK2(u0,x0,x,h):
	u=u0
	x0=0
	N=round((x-x0)/h) #step number
	U=[u0]
	X=[x0]
	a=1
	for i in range  (0,N):
		K1=h*func(u0,x0)
		K2=h*func(x0+a*h,u+a*K1)
		u=u+(1-1/2*a)*K1+(1/2*a)*K2
		x0=x0+h
		U.append(u)
		X.append(x0)
		
	return X,U,u

x0=0
x=3 #given that 0<= x <= 3
u=1
h=0.01
x,u,u_soln=RK2(u,x0,x,h)
print ("solution:", round(u_soln,4))
plt.title('Runge-Kutta 2nd Order')
plt.xlabel('x')
plt.ylabel('u')
plt.plot(x, u, 'r-', label="u,x")
plt.grid(True)
plt.legend()
plt.show()