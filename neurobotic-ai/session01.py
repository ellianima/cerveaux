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



# 0 Dimensional Arrays are called scalars
# They are the simplest form of data, single value
# no axes, no rows, no columns, a 0-D array is a single point in space!!

arr = np.array(42)


print(arr)
#output: 42

print(f"Dimensions: {arr.ndim}")

"""
ndim is a property of the array that tells us how many dimensions it has
which is zero! or 0

why we use 0-D arrays instead of a simple number?
because they can be used in mathematical operations and functions
that expect an array as input, even if it's just a single value
"""

arr2 = np.array([42])
print(arr2[0])

"""
The two code below are the same thing
"""
arr = np.array(42)
print(np.array(42).ndim)
print(arr.ndim)

"""
checking ID tags now for 0-D arrays
"""
print("Checking ID tags for 0-D arrays")
arr = np.array(42)
print(arr.ndim) #total num of dimensions
print(arr.size) #total num of elements
print(arr.shape) #describes length, a 0-D array has no shape (rows, columns, etc) so it returns an empty tuple


