
# python 3

import numpy as np
import math

#given matrices (arrays):
arr_left=[[1,-1,2,1],[3,2,1,4],[5,-8,6,3],[4,2,5,3]]
x1,x2,x3,x4=0,0,0,0
X=[x1,x2,x3,x4]
arr_right=[1,1,1,-1]

#definitions:
scale=np.amax(np.absolute(arr_left),1)
index=np.arange(len(arr_left))

dummy=index
residue=[0,0,0,0]

for i in range (len(index)-1):
	abs_arr_left=np.absolute(arr_left)
	for j in (index):
		residue[j]=(abs_arr_left[index[j]][i]/scale[index[j]])
	for j in range(i):
		residue[j]=-1 #converting the checked values to -1
	relocate_index=np.argmax(residue) #to find max element
	temp=index[relocate_index] #defining temprorary element to swap
	index[relocate_index]=index[i]
	index[i]=temp
	dummy=np.delete(dummy,np.where(dummy==index[i])) #get rid of i'th element of index array
	dummy2=index[i]

	for a in (dummy):
		C=(arr_left[a][i])/(arr_left[dummy2][i]) #C:constant for elimination
		arr_left[a]=arr_left[a]-np.multiply(C,arr_left[dummy2]) #multiplying matrix with constant
		arr_right[a]=arr_right[a]-(C*arr_right[dummy2])

M=len(index)-1
for i in index:
	sum=0
	for j in range (len(index)):
		sum+=(arr_left[index[i]][M-j])*(X[M-j])
	X[i]=(arr_right[index[i]]-sum)/(arr_left[index[i]][i])
print ("Solution array is: ", X)

#residue calculations
arr_left=[[1,-1,2,1],[3,2,1,4],[5,-8,6,3],[4,2,5,3]]
arr_right=[1,1,1,-1]

residue=np.dot(arr_left,X)-arr_right
print ("Residue: ", residue)