
# python 3

#Q-1 part a
import math


# f is the desired function, x is initial guess, df is the derivative of f
# eps is error
def Newton_Method(f,x,df,eps): #function to find roots using newton-raphson method
	while True:
		dx=-(f(x)/df(x)) #dx is the differnce between iterated x values
		x=x+dx #iterating variable x
		if (abs(dx) < eps) : #convergence criteria
			return x
			break

#initials
def func(x): #Q-1 part a given function
	return math.exp((-x)/2)-2*x*math.cos(x)+5

def deriv(x): #derivative of Q-1 part a given function
	return math.exp(-x/2)/2+2*x*math.sin(x)-2*math.cos(x)

print("The root found with newton-raphson method is:" ,Newton_Method(func,5,deriv,0.001))



#Q-1 partb
# f is the desired function, x0 and x1 are initial guesses
# eps is error
def secant_method(x0,x1,f,eps):
	for i in range(0,500):
		x2=x1-f(x1)*((x1-x0)/(f(x1)-f(x0))) #next guess for the value of xi+1
		if (abs(x2-x1) < eps): #convergence criteria
			return x2
			break
		else:
			x0, x1 = x1, x2   #assigning new values for the loop

print("The root found with secant method is: ", secant_method(5,5.1,func,0.001))


#Q-2
def force(x): #given function for Q-2
	#constans
	k=1/(math.pi*4*8.85*10**(-12))
	q=2*10**(-5)
	Q=2*10**(-5)
	a=0.9
	return ((k*q*Q*x)/(x**2+a**2)**(3/2))-1

def deriv_force(x): #derivative of force function
	k=1/(math.pi*4*8.85*10**(-12))
	q=2*10**(-5)
	Q=2*10**(-5)
	a=0.9
	return k*q*Q*(a**2-2*x**2)/(a**2+x**2)**(5/2)

print ("roots for question 2")
print("The root found with secant method is: ", secant_method(0.83,0.75,force,0.0001))
print("The root found with secant method is: ", secant_method(0.30,0.25,force,0.0001))
print()

print("The root found with newton-raphson method is:" ,Newton_Method(force,0.75,deriv_force,0.001))
print("The root found with newton-raphson method is:" ,Newton_Method(force,0.30,deriv_force,0.001))

#I tried to find an estimated root by looking at the plot below:

'''import matplotlib.pyplot as plt 
from numpy import *
t = arange(-5,5,0.1)
plt.plot(t,force(t))
plt.grid(True)
plt.show()

'''