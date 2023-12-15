import numpy as np

# x1 + x2 = 2200. 1.5x1 + 4x2 = 5050  
# A = [[1,1], [1.5,4.0]]  b = [2200, 5050]  x =[x1, x2]
# A * x = b, x = A-1b (inverse of A times b)


A = np.array([[1,1], [1.5,4.0]])
b = np.array([2200, 5050])

x = np.linalg.inv(A).dot(b)  # inverse of A: np.linalg.inv(A)   dot product of b: .dot(b)
print(x)


x = np.linalg.solve(A, b)  