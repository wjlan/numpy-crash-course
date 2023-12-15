import numpy as np

a = np.array([1,2,3])
b = a
b[0] = 42
print(b)
print(a)

c = np.array([1,2,3])
d = c.copy()
d[0] = 42
print(d)
print(c)
