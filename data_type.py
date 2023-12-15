import numpy as np

x = np.array([1,2])
print(x)
print(x.dtype)  # -> int64 means int with 64 bits/ 8 bytes

x = np.array([1.0,2.0])
print(x)
print(x.dtype)

x = np.array([1.0,2.0], dtype=np.int64)
print(x)
print(x.dtype)
