
# python 3

import numpy as np
import math 
#import matplotlib.pyplot as plt

def func (x):
	return math.exp((-(x-69)**2)/5.6) * (2.8 * math.sqrt(2*math.pi) )**(-1)

lower_lim=150*0.3937 # converting cm to inches by multiplying given lengths with 0.3937
upper_lim=182*0.3937
n=10000 #number of intervals

def Simpson_method(a,b,func,n): #computing the simpson method here
	h=(b-a)/n
	even=0
	odd=0
	for i in range (1,n):
		if (i%2)==0:
			even=func(a+h*i)+even #redefining even
		else:
			odd=func(a+h*i)+odd #redefining odd
	Integral=(h/3)*(func(a)+odd*4+even*2+func(b)) #concluding approximation
	return Integral
print ("Integration calculated by Simpson method is: ", Simpson_method(lower_lim,upper_lim,func,n))
print ("The probability is: ",round(100*Simpson_method(lower_lim,upper_lim,func,n), 1) , "percent")