import numpy as np

a = np.array([10, 19, 30, 41, 50, 61])
print(a)
b = [1,3,5]
print(a[b])

even = np.argwhere(a%2==0).flatten()
print(a[even])