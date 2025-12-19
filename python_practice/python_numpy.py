import numpy as np
from numpy.ma.extras import vstack

print(np.arange(10))
print(type(np.arange(10)))


arr = np.arange(10)
print(arr.shape)

array1 = np.array([1,2,3,4,5])
print(array1)
print(type(array1))

array1 = np.array([[1,2,3,4,5]])
print(array1)
print(array1.shape)

# random
arr2 = np.random.random(size=10)
print(arr2)
arr3 = np.random.random(size=(3,4))
print(arr3)
arr4 = np.random.randint(3,14,size=10)
print(arr4)

print('------------------')
arr_zero = np.zeros(5)
arr_one = np.ones(5)
arr_emp = np.empty((2,3))
print(arr_emp)

print('-----------line space')
arr_line = np.linspace(0,5,6)
print(arr_line)

print('--------reshape----------')
arr = np.arange(12)
print(arr)
arr_reshape = arr.reshape(3,4)
print(arr_reshape)
print(arr_reshape.reshape(2,2,3))

print('--------hstack,vstack:拼接----------')
a = np.array([[1,2,3],[4,5,6]])
b = np.array([['a','b','c'],['d','e','f']])
print(np.hstack([a,b]))
print(np.vstack([a,b]))

