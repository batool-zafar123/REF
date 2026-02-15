import numpy as np

matrix = np.array([[-4, 1, 1, 0],
           [1, -4, 0, 1],
           [1, 0, -4, 1],
           [0, 1, 1, -4]], dtype = float)

print("Original matrix:\n", matrix)

rank = np.linalg.matrix_rank(matrix)

print("Rank = ", rank)