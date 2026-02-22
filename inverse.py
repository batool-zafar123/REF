import numpy as np

A = np.array([
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
], dtype=float) # Use float type for numerical stability

if np.linalg.det(A) == 0:
    print("The matrix is singular and has no inverse.")
else:
    # Calculate the inverse of the matrix
    A_inv = np.linalg.inv(A)

    # Print the original matrix and its inverse
    print("Original Matrix A:")
    print(A)
    print("\nInverse of Matrix A:")
    print(A_inv)