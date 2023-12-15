import numpy as np
# print(np.__version__)

l = [1,2,3]
a = np.array([1,2,3])
# print(a)
# print(a.shape) # one dimension with 3 elements
# print(a.dtype) # data type is int64 means int(each element is 64 bits)
# print(a.ndim) # number of dimension
# print(a.size) # total number of elements
# print(a.itemsize) # size in bytes of each element, 64 bits = 8 bytes

# print(a[0])
# a[0] = 10
# print(a)

# b = a * np.array([2,0,2])
# print(b)

# l.append(4)
# print(l)
# a.append(4)
# print(a)

l = l + [4]
print(l)
a = a + np.array([4])
print(a)   # [5 6 7] each element adds 4 -> called broadcasting


