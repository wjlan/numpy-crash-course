import numpy as np

# generating arrays: the defalt data type here is a float
a = np.zeros((2,3))
print(a)

a = np.ones((2,3))
print(a)
print(a.dtype)   

a = np.full((2,3), 5.0)
print(a)

a = np.eye(3)  # create a matrix where the diagonal is filled with ones
print(a)

a = np.arange(20)
print(a)

a = np.linspace(0,10,5)  # all of the numbers between the start 0 and end 10 are equally spaced
print(a)
