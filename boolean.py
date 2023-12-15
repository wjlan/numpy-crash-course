import numpy as np

a = np.array([[1,2], [3,4], [5,6]])
# print(a)
bool_idx = a > 2
# print(bool_idx)
print(a[bool_idx])  # This uses the boolean mask to index the original array a. Only the elements corresponding to True values in the boolean mask are selected
print(a[a>2])

b = np.where(a>2, a, 0)
print(b)