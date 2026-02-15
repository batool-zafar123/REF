import numpy as np

# Define the matrix as a NumPy array (example: 3x3 matrix)
matrix = np.array([[2/3, 1/3, 2/3],
                   [-2/3, 2/3, 1/3],
                   [1/3, 2/3, -2/3]])

# Calculate the determinant
det = np.linalg.det(matrix)

print("The matrix is:\n", matrix)
print("The determinant is:", det)
