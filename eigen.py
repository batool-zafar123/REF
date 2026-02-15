import numpy as np

A = np.array([[-3, 0, 4, 2],
              [0, 1, -2, 4],
              [2, 4, -1, -2],
              [0, 2, -2, 3]])

# Calculate eigenvalues and eigenvectors
# The 'eig' function returns a tuple of (eigenvalues, eigenvectors)
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the results
print("Matrix A:")
print(A)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors (stored as columns):")
print(eigenvectors)

# Optional: Verify the results for the first eigenvalue and eigenvector
# The equation Ax = lambda * x should hold true
# lambda1 = eigenvalues[0]
# v1 = eigenvectors[:, 0] # Get the first eigenvector (first column)

# Ax = np.dot(A, v1)
# lambda_x = lambda1 * v1

# print("\nVerification for the first eigenvector/eigenvalue:")
# print("Ax:", Ax)
# print("lambda * x:", lambda_x)
