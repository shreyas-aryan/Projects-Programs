#7ways to create arrays
import numpy as np
import sys
arr1=np.array([2,3,4,5,6,7])#array
print(arr1)
print(type(arr1))
arr2=np.linspace(1,10,6,dtype=int).reshape(3,2)#linspace
print(arr2)
arr3=np.arange(1,10,2)#arange
print(arr3)
arr4=np.ones((5,4),"int")#ones
print(arr4)
arr5=np.zeros((3,6),"int")#zeros
print(arr5)
arr6=np.random.rand(10)#random.rand
print(arr6)
arr7=np.logspace(1,10,5)#logspace
print(arr7)
print(arr1.itemsize)
print(sys.getsizeof(arr1))
arr8=arr1.reshape(3,2)#reshape
print(arr8)
print(arr8.shape)#returns shape of arr dimensions
print()
print(arr8.sum())#returns sum
print(arr8.sum(axis=0))#summing values of every row
print(arr8.sum(axis=1))#summing values of every cols
print(np.add(arr8,arr2))#adding, vector
print(np.multiply(arr8,arr2))#multiply vector
print(np.subtract(arr8,arr2))
print(np.divide(arr8,arr2))
print(np.remainder(arr8,arr2))
print(arr8[0,1])#indexing
print()
print()
print(arr8)
print(arr8[1:2,1:])#slicing
print(arr8[0:1])
#arr8[rows:endrow,cols:endcols]
a_sub=arr8[1:,0:1]#subset
print()
print(a_sub)
a_sub[1]=100
print(a_sub)
print(arr8)#main array updated
a=np.append(arr8,[[10,20]],axis=0)#append rows
print(a)
a=np.append(arr8,[[10],[20],[30]],axis=1)#append cols
print(a)
a=np.insert(arr8,1,[10,20,30],axis=1)#insert col at index
print(a)
a=np.delete(arr8,1,axis=0)#dlete row
print(a)
