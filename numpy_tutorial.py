import numpy as np
import time
import sys
SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("python list took: ",(time.time()-start)*1000)

#numpy array
start=time.time()
result= a1+a2
print("numpy took: ", (time.time()-start)*1000)


import numpy as np

#list in numpy
a = np.array([5,6,9])
print(a[0])
print(a[1])

#two dimensional array
b=np.array([[1,2], [3,4],[5,6]])

#to print number of dimensions
print(b.ndim)

#to print the itemsize
print(b.itemsize)

#to print the type of data
print(b.dtype)

#to print the total number of element
print(b.size)

#zeros () function
print(np.zeros((3,4)))

#ones() function
print(np.ones((3,4)))

#arange function
print(np.arange(1,5))
print(np.arange(1,19,2))


