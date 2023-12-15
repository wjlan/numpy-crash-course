import numpy as np

a = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors)

# e_vec * e_val = A * e_vec
b = eigenvectors[:,0] * eigenvalues[0]
print(b)
c = a @ eigenvectors[:,0]
print(c)

# To compare the array if they are equal
print(np.allclose(b,c))