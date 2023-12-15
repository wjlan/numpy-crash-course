import numpy as np

a = np.arange(1, 7) # create a 1D array from 1 to 6
print(a)
print(a.shape)  # -> (6,) it is only 1D
b = a.reshape(3, 2) # reshape into 3 rows and 2 columns
print(b)

#  a method to create a new axis in the data
b = a[np.newaxis, :]
print(b)
print(b.shape)
b = a[:, np.newaxis]
print(b.shape)
print(b)