import numpy as np

# x = np.array([[1,2,3], [4,5,6],[1,2,3], [4,5,6]])
# a = np.array([1,0,1])

# y = x + a
# print(y)

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)
print(a.sum())  #  a.sum(axis=None)  axis=None is by default, will calculate overall sum
print(a.sum(axis=0))  # calculate along the row, we get one sum entry for each column
print(a.sum(axis=1))  # calculate along the column, we get one sum entry for each row
print(a.mean(axis=0))
print(a.mean(axis=1))
print(a.var)   
print(a.std)   # np.std(a, axis=None)
# a.min, a.max


