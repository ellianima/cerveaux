import numpy as np
#
#arr = np.array([1, 2, 3, 4, 5])
#
#print(arr)
#
#print(type(arr))
#
#heart_rates = np.array([70, 72, 75, 80])
#
#print(type(heart_rates))
#
#data_a = [1, 2, 3]
#data_b = (1, 2, 3)
#
#arr_a = np.array(data_a)
#arr_b = np.array(data_b)
#
#print(type(arr_a))
#print(type(arr_b))
#
#
#
#
## 0 Dimensional Arrays are called scalars
## They are the simplest form of data, single value
## no axes, no rows, no columns, a 0-D array is a single point in space!!
#
#arr = np.array(42)
#
#
#print(arr)
##output: 42
#
#print(f"Dimensions: {arr.ndim}")
#
#"""
#ndim is a property of the array that tells us how many dimensions it has
#which is zero! or 0
#
#why we use 0-D arrays instead of a simple number?
#because they can be used in mathematical operations and functions
#that expect an array as input, even if it's just a single value
#"""
#
#arr2 = np.array([42])
#print(arr2[0])
#
#"""
#The two code below are the same thing
#"""
#arr = np.array(42)
#print(np.array(42).ndim)
#print(arr.ndim)
#
#"""
#checking ID tags now for 0-D arrays
#"""
#print("Checking ID tags for 0-D arrays")
#arr = np.array(42)
#print(arr.ndim) #total num of dimensions
#print(arr.size) #total num of elements
#print(arr.shape) #describes length, a 0-D array has no shape (rows, columns, etc) so it returns an empty tuple
#
#
#print(arr.dtype) 
##data type of the array, in this case it's int64 (integer) because 42 is an integer
##int64 is a data type that can store integers up to 64 bits in size, which is a very large range of nubmers
#
#
#temp = np.array(42.0)
#print(temp.dtype) #checks datatype
##data type of the array, in this case it's float64 (floating point number) because 42.0 is a floating point number
#
#
#print(np.array(25.9, dtype=int)) #forcing and truncating
##converting a floating point number to an integer using the dtype parameter, it will truncate the decimal part and return 25
#
#precise_temp = np.round(25.9)
#final_temp = precise_temp.astype(int)
#print(final_temp)
#
#
#initial_price = np.round(105.99)
#final_price = initial_price.astype(int)
#print(final_price)
#
#
#"""
#.ndim checks the dimensions of an array
#.size checks how many items inside
#.shape checks the shape on rows or columns
#.dtype checks the data type of an array
#
#The zero dimensional array is a single value with no shape, no rows, no columns
#and it can be used in mathematical operations and functions that expect an array as input
#even if it's just a single value
#
#
#
#EL5: like a single atom,
#represents ONE individual value
#ONE piece of data, nothing to separate
#
#"""
#
## integer example
#print(np.array(100))
#
##float example
#
#print(np.array(98.6))
#
##boolean example
#
#print(np.array(True))
#
##string example
#
#print(np.array("Alpha"))
#"""
#0-D array is the content itself
#
#1-D and more is more like the container
#"""
#
#
#
## 0-D = scalars
#
#arr = np.array([1, 2, 3, 4, 5])
#print(f"First Array | Dimensions: {arr.ndim}")
##this is a 1-D array which is also a vector, it has 1 dimension, a single row of data
#
#arr = np.array([[1, 2, 3], [4, 5, 6]])
#print(f"Second Array | Dimensions: {arr.ndim}")
##this is a 2-D array which is also a matrix, it has 2 dimensions, rows and columns
#
#arr = np.array([[[1, 3, 4], [5, 6, 7]], [[8, 9, 10], [11, 12, 13]]])
#print(f"Third Array | Dimensions: {arr.ndim}")
##this is a 3-D array which is also a tensor, it has 3 dimensions, rows, columns and depth
#
#
#
#
#one_d_array = np.array([1, 2, 3, 4, 5])
#print(one_d_array)
#
##2D arraws with 2 rows and 3 columns
#two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
#print(two_d_array)
#
#
#print(one_d_array.shape)
#print(two_d_array.shape)
#
#c = np.array([
#            [[1, 2, 3], [4, 5, 6]],
#            [[7, 8, 9], [10, 11, 12]]
#              ])
#
#print(c.shape)
#
#c = np.array([[[1, 2], [3, 4]],
#            [[5, 6], [7, 8]]])
#print(c.shape)
#

"""
Outer layer in c variable is the tensor
Middle layer in c variable is the matrix
Inner layer in c variable is the vector

outer tensor layer has 2 matrices and each matrix has 2 vectors and each vector has 2 scalars (or values)

is my explanation to it
"""


print(np.zeros((2, 3)))
#the code above made a 2-D array with 2 rows and 3 columns filled with zeros, as floats?!

print(np.ones((2, 3)))
#the code above made a 2-D array with 2 rows and 3 columns filled with ones, as floats?!

print(np.full((2, 3), 7))
#the code above made a 2-D array with 2 rows and 3 columns filled with the number 7, as integers?!

print(np.arange(0, 10, 2))
#the code above made a 1-D array from start inclusive 0 to stop exccluse 10 with a step of 2.
#what does arange mean? it stands for array range, it creates an array of evenly spaced values within a given interval, defined by the start, stop, and step parameters.

print(np.linspace(0, 1, 5))
#first it created a 1 dimensional array in float type.. now what I got from it is that it made it so that from 0 to 1, it made it into 5 evenly spaced values


print(np.linspace(0, 10, 3))
print(np.arange(0, 10, 3))

"""
linspace and arange are both functions in NumPy that generate arrays of evenly spaced values, but they do so in different ways:

"""