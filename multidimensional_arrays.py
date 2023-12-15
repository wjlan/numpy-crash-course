import numpy as np

a = np.array([[1,2], [3,4]])
print(a)
print(a.shape) # (2, 3) -> 2 by rows 3 by columns
print(a[0][0])
print(a[0,0]) # np array index
print(a[:,0]) # np array slicing, all the row, first column -> [1 3]

print(np.linalg.inv(a)) # calculate inverse matrix
print(np.linalg.det(a)) # calculate determinant
print(np.diag(a))  # calculate diagonal 