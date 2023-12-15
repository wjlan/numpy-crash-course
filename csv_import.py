import numpy as np

# np.loadtxt 
# np.genfromtxt

data = np.loadtxt('spambase.csv', delimiter=",", dtype=np.float32)
print(data)
print(data.shape)

data = np.genfromtext('spambase.csv', delimiter=",", dtype=np.float32)
print(data)
print(data.shape)