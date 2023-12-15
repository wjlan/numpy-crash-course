import numpy as np

# # apppend element

# a = np.array([[1,2], [3,4]])
# print(a)
# b = np.array([[5,6]])
# c = np.concatenate((a, b), axis = 0)
# print(c)
# c = np.concatenate((a, b), axis = None)  # Concatenate along a new axis (axis=None, which means flatten)
# # arrays are flattened before concatenation. It essentially treats both arrays as one-dimensional arrays and concatenates them along a new axis. The resulting array will be a flattened 1D array
# print(c)

# d = np.concatenate((a, b.T), axis = 1)
# print(d)
# # np.concatenate((a, b.T), axis=1) concatenates these two arrays along axis 1 (columns). This results in a new array d where the elements from b.T are added as new columns to the right of the original array a


# a1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
# b1 = np.array([[0,0,0]])
# e = np.concatenate((a1, b1.T), axis =1)
# print(e)

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.hstack((a,b))  # concatenate horizontally with one columnn using hstack
d = np.vstack((a,b))  # concatenante vertically into two rows
print(c) # concatenate
print(d) 
