import sympy

# Define your matrix (use float or int values as needed)
# Example matrix:
matrix_data = [[1, 0, 0, -1],
               [0, 0, 0, 1],
               [0, 0, 0, 0]]

# Convert to a sympy Matrix object
m = sympy.Matrix(matrix_data)

# Get the reduced row echelon form and the pivot columns
rref_matrix, pivot_columns = m.rref()

print("Original Matrix:")
print(m)
print("\nReduced Row Echelon Form (RREF):")
print(rref_matrix)
