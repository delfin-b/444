import math 
import matplotlib.pyplot as plt
import numpy as np


N=(np.log(40)-np.log(0.05))/np.log(2) #for part a in order to find how many iterations we have to do
print("we have to iterate", int(N), "times") #N=number of iterations to find the root
def osf(Ta): #i wrote concentration of oxygen as a function
	c1=-139.34411 #for the sake of simplicity
	c2= 1.575701*10**5
	c3=-6.642308*10**7
	c4=1.243800*10**10
	c5=-8.621949*10**11
	return math.exp((c1+ (c2/Ta) + (c3/Ta**2) + (c4/Ta**3) + (c5/Ta**4)))-np.log(10) ##i checked for odf=10 but 8 and 12 also work

def bisect(x1,x2): #bisection method function

	count=0 #i added counter to determine the number of iterations
	while ((x2-x1)>=0.05): # i set the error range as 0.05
		x3= (x1+x2)/2
		if (osf(x3)==0.0):
			break
		if (osf(x3)*osf(x1)<0):
			x2=x3
		else:
			x1=x3
		count=count+1
		
	print (" the root is : " , "%.4f"%x3)
	print ("bisection is applied for", count, "times.")
	


x1=0 # initial values for temperature
x2=40
y1=14.621
y2=6.413

Ta1=x1+273.15
Ta2=x2+273.15
bisect(Ta1, Ta2)

Ta = np.arange(start=0, stop=40, step=1)
y = []

for i in Ta:
	
	a = osf(i+273.15)
	y = np.append(y,a)

plt.xlabel('Ta') 
plt.ylabel('osf(Ta)')
plt.title('osf(Ta) versus T graph') # giving our plot a name
plt.plot(Ta, y, marker='.', color='r', label="not fitted", linestyle='-') 


plt.show()  