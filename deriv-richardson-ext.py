
# python 3

import numpy as np
import math

def func(x): #function is given
	return math.pow(x,math.cos(x))

def Central_Diff(h): #function of central difference method
	return (func(x+h)-func(x-h))/(2*h)

def fi(h,n): #fi for richardson extrapolation method
	return Central_Diff(h/2**n)

#main
n=5
m=5
x=0.6
h=0.1
def Deriv(n,m): #recursive function for derivation (i've learned reursive functions from ceng301 course in c++ hocam)
	if m==0:
		D=fi(h,n)
		return D
	else:
		D=Deriv(n,m-1) + ((Deriv(n,m-1)-Deriv(n-1,m-1))*(1/((4**m)-1))) #here is the recursion
		return D


#print (func(x))
#print (fi(h,n))
#print (Central_Diff(h))
#print (Deriv(n,m))
print ("Derivative of f(x)=x**cos(x) at x=", x, "with step size:", h, "and n,m",n,m,"is:", Deriv(n,m))