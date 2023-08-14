
# python 3

import math
import numpy as np

def func(x): #given function
	return math.exp(x)*math.cos(x)

a=0.5 #limits
b=1.5

def Gauss_Q(func,a,b): #Gaussian Quadrature with 2 points
	x1=((b-a)/2)*(-0.7745966692)+((b+a)/2) #transforming limits and gauss points
	x2=((b-a)/2)*0.7745966692+((b+a)/2)
	c1=((b-a)/2) #constant coefficients
	c2=((b-a)/2)
	integral=c1*func(x1)+c2*func(x2) #summation approximation
	print ("integral: ", integral)
	return integral

Gauss_Q(func,a,b)