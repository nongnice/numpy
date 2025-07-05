import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a=np.array([[1,2,3,4],[5,6,7,8,],[9,10,11,12]])
print (a.shape)
print(a)

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b=a[:2,1:3]
print(b)

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.


print(a[0,1])
print('this is a b\n', b)
b[0,0]=77
print('this is a b\n', b)
print(a[0,1])