import numpy as np
import sympy as sp

Vec = np.array([[1, 1, 1, 5],
              [1, 2, 0, 3],
              [2, 1, 3, 9],
              [2, 4, -5, 0]])

# Convert the NumPy array to a SymPy Matrix and apply echelon_form()
Vec_echelon = sp.Matrix(Vec).echelon_form()

print("Original Matrix:")
print(Vec)
print("\nRow Echelon Form using SymPy:")
print(Vec_echelon)
