import numpy as np
import matplotlib.pyplot as plt


def main():

    matrix = matrix_input()
    
    system(matrix)


def REF(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    pivot_row = 0
    for i in range(columns): 
        # Finding Pivot
        search_row = pivot_row
        pivot = matrix[pivot_row][i]
        while abs(pivot) < 1e-9:
            search_row += 1
            if search_row == rows:
                break  # No pivot found
            pivot = matrix[search_row][i]

        if search_row != pivot_row and search_row < rows:
            matrix[pivot_row], matrix[search_row] = matrix[search_row], matrix[pivot_row]
            pivot = matrix[pivot_row][i]
        if abs(pivot) > 1e-9:
            # Eliminating entries below pivot
            for j in range(pivot_row + 1, rows):
                mult = matrix[j][i] / pivot
                matrix[j] = [a - mult * b for a, b in zip(matrix[j], matrix[pivot_row])]
                matrix[j] = [0.0 if abs(val) < 1e-9 else val for val in matrix[j]]
         
            pivot_row += 1
            if pivot_row == rows:
                break


def REF_1(matrix):
    for row in matrix:
        for val in row:
            if abs(val) > 1e-9:
                divisor = val
                for j in range(len(row)):
                    row[j] /= divisor
                    if abs(row[j]) < 1e-9:
                        row[j] = 0.0
                break


def RREF(matrix):
    p = len(matrix)
    n = len(matrix[0])
    
    for i in range(p - 1, -1, -1):
        pivot_column = -1
        for k in range(n):
            if abs(matrix[i][k]) > 1e-9:
                pivot_column = k
                break
        if pivot_column == -1:
            continue

        for j in range(i - 1, -1, -1):
            mult = matrix[j][pivot_column]
            matrix[j] = [a - mult * b for a, b in zip(matrix[j], matrix[i])]
            matrix[j] = [0.0 if abs(val) < 1e-9 else val for val in matrix[j]]

                

def system(matrix):
    print("Original Matrix: ")
    display(matrix)
    plot_matrix = [row[:] for row in matrix]
    REF(matrix)
    REF_1(matrix)
    RREF(matrix)
    print("RREF Matrix:")
    display(matrix)

    if check_consistent(matrix):
        print("System is consistent.\n")
        non_zero_rows = 0
        for row in matrix:
            if not all(abs(x) < 1e-9 for x in row):
                non_zero_rows += 1
        
        num_vars = len(matrix[0]) - 1
        if non_zero_rows == num_vars:
            for i in range(len(matrix[0])-1):
                print(f"The variable X{i+1} = {matrix[i][-1]:.4f}.")
            if len(matrix) == 2 and len(matrix[0]) == 3:
                line_plot(matrix, plot_matrix) 
            else:
                pass
            
        else:
            print("The system has infinitely many solutions. (Logic Pending)\n")
    else:
        print("System is inconsistent. Solution not possible.\nPlot not available.\n")


def check_consistent(matrix):
    rows = len(matrix)
    for i in range(rows):
        if all(abs(x) < 1e-9 for x in matrix[i][:-1]) and abs(matrix[i][-1]) > 1e-9:
            return False
    return True


def display(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        print("[ ", end = "") if i == 0 else print("  ", end = "")
        for j in range(c):
            val = matrix[i][j]
            if abs(val) < 1e-9: val = 0.0
            if not j == c-1:
                print(f"{val:.4f}", "   ", end = "") 
            else:
                print(f"{val:.4f}", "", end = "")
        print("]") if i == r-1 else print()
    print()


def matrix_input():
    # INPUT from user--->
    p = int(input("How many equations? "))
    n = int(input("How many variables? ")) + 1
    matrix = []
    print()
    for i in range(p):
        row = []
        for j in range(n):
            if not j == n-1:
                row.append(float(input(f"Enter entry # {i+1}{j+1}: ")))
            else:
                row.append(float(input(f"Enter constant # {i+1} / entry # {i+1}{j+1}: ")))
        matrix.append(row)
        print()
    return matrix

def line_plot(rref, matrix):
    cx = rref[0][2]
    x = np.linspace(cx - 10, cx + 10, 200)

    plt.figure(figsize=(8, 6))
    
    # Equation 1: a1*x + b1*y = c1
    a1, b1, c1 = matrix[0][0], matrix[0][1], matrix[0][2]
    if abs(b1) > 1e-9:
        y1 = (c1 - a1 * x) / b1
        plt.plot(x, y1, label=f"{a1}x + {b1}y = {c1}", color='blue')
    elif abs(a1) > 1e-9:
        plt.axvline(x=c1 / a1, label=f"x = {c1 / a1:.2f}", color='blue')

    # Equation 2: a2*x + b2*y = c2
    a2, b2, c2 = matrix[1][0], matrix[1][1], matrix[1][2]
    if abs(b2) > 1e-9:
        y2 = (c2 - a2 * x) / b2
        plt.plot(x, y2, label=f"{a2}x + {b2}y = {c2}", color='red')
    elif abs(a2) > 1e-9:
        plt.axvline(x=c2 / a2, label=f"x = {c2 / a2:.2f}", color='red')

    # Plot intersection point if available
    ix, iy = rref[0][2], rref[1][2]
    plt.plot(ix, iy, 'go', label=f"Solution ({ix:.2f}, {iy:.2f})")

    plt.grid(True, ls=":")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("System of Linear Equations (2D Visualization)")
    plt.legend()
    plt.show()


def _normalize_matrix(matrix):
    """Converts a matrix (list of lists or numpy array) to a float list of lists."""
    if hasattr(matrix, "tolist"):
        matrix = matrix.tolist()
    return [[float(val) for val in row] for row in matrix]


def _input_matrix_general():
    """Interactive input for general matrices (REF / RREF)."""
    print("--- Matrix Dimensions ---")
    rows = int(input("How many rows? "))
    cols = int(input("How many columns? "))
    matrix = []
    print("\n--- Enter Matrix Elements ---")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Enter entry [{i+1}, {j+1}]: ")))
        matrix.append(row)
        print()
    return matrix


def _input_system():
    """Interactive input for linear systems (augmented matrices)."""
    print("--- Linear System Equations ---")
    p = int(input("How many equations? "))
    n = int(input("How many variables? "))
    matrix = []
    print("\n--- Enter Coefficients and Constants ---")
    for i in range(p):
        row = []
        for j in range(n):
            row.append(float(input(f"Eq #{i+1} - Coefficient for X{j+1}: ")))
        row.append(float(input(f"Eq #{i+1} - Constant: ")))
        matrix.append(row)
        print()
    return matrix


def _input_plot_system():
    """Interactive input specifically for 2D line plotting (2 equations, 2 variables)."""
    print("--- 2D Linear System (2 Equations, 2 Variables) ---")
    matrix = []
    for i in range(2):
        row = []
        row.append(float(input(f"Equation #{i+1} - Coefficient for X: ")))
        row.append(float(input(f"Equation #{i+1} - Coefficient for Y: ")))
        row.append(float(input(f"Equation #{i+1} - Constant: ")))
        matrix.append(row)
        print()
    return matrix


# =====================================================================
# Beginner-Friendly Public Functions
# =====================================================================

def to_ref(matrix=None, show_steps=False):
    """Converts a matrix into Row Echelon Form (REF).
    
    Parameters:
        matrix: list of lists or numpy array (optional). If None, prompts interactively.
        show_steps: bool, whether to print the matrix before and after conversion.
        
    Returns:
        list of lists: The matrix in Row Echelon Form.
    """
    if matrix is None:
        matrix = _input_matrix_general()
    mat = _normalize_matrix(matrix)
    
    if show_steps:
        print("Original Matrix:")
        display(mat)
        
    REF(mat)
    
    if show_steps:
        print("Row Echelon Form (REF):")
        display(mat)
        
    return mat


def to_rref(matrix=None, show_steps=False):
    """Converts a matrix into Reduced Row Echelon Form (RREF).
    
    Parameters:
        matrix: list of lists or numpy array (optional). If None, prompts interactively.
        show_steps: bool, whether to print the matrix before and after conversion.
        
    Returns:
        list of lists: The matrix in Reduced Row Echelon Form.
    """
    if matrix is None:
        matrix = _input_matrix_general()
    mat = _normalize_matrix(matrix)
    
    if show_steps:
        print("Original Matrix:")
        display(mat)
        
    REF(mat)
    REF_1(mat)
    RREF(mat)
    
    if show_steps:
        print("Reduced Row Echelon Form (RREF):")
        display(mat)
        
    return mat


def solve_system(matrix=None, plot=False, show_steps=True):
    """Solves a system of linear equations from an augmented matrix [A | B].
    
    Parameters:
        matrix: list of lists or numpy array (optional). If None, prompts interactively.
        plot: bool, whether to display a 2D line plot for 2x3 systems.
        show_steps: bool, whether to print steps and formatted solutions.
        
    Returns:
        dict | str | None:
            - dict with variable values (e.g. {"X1": 1.0, "X2": 2.0}) for unique solution.
            - "infinitely many solutions" if system has infinite solutions.
            - None if system is inconsistent.
    """
    if matrix is None:
        matrix = _input_system()
        
    mat = _normalize_matrix(matrix)
    plot_matrix = [row[:] for row in mat]
    
    if show_steps:
        print("Original Augmented Matrix:")
        display(mat)
        
    REF(mat)
    REF_1(mat)
    RREF(mat)
    
    if show_steps:
        print("RREF Matrix:")
        display(mat)
        
    if not check_consistent(mat):
        if show_steps:
            print("System is inconsistent. No solution exists.\n")
        return None
        
    non_zero_rows = 0
    for row in mat:
        if not all(abs(x) < 1e-9 for x in row):
            non_zero_rows += 1
            
    num_vars = len(mat[0]) - 1
    if non_zero_rows == num_vars:
        solutions = {}
        for i in range(num_vars):
            solutions[f"X{i+1}"] = mat[i][-1]
            if show_steps:
                print(f"The variable X{i+1} = {mat[i][-1]:.4f}")
        if show_steps:
            print("System is consistent with a unique solution.\n")
            
        if plot:
            if len(mat) == 2 and len(mat[0]) == 3:
                line_plot(mat, plot_matrix)
            elif show_steps:
                print("Note: 2D line plot is only available for 2x3 systems (2 equations, 2 variables).\n")
                
        return solutions
    else:
        if show_steps:
            print("The system has infinitely many solutions. (Parametric logic pending)\n")
        return "infinitely many solutions"


def is_consistent(matrix=None, verbose=True):
    """Checks whether a linear system (augmented matrix) is consistent.
    
    Parameters:
        matrix: list of lists or numpy array (optional). If None, prompts interactively.
        verbose: bool, whether to print the consistency status.
        
    Returns:
        bool: True if system has one or more solutions, False if inconsistent.
    """
    if matrix is None:
        matrix = _input_system()
        
    mat = _normalize_matrix(matrix)
    REF(mat)
    REF_1(mat)
    RREF(mat)
    
    consistent = check_consistent(mat)
    if verbose:
        if consistent:
            print("System is consistent (has at least one solution).\n")
        else:
            print("System is inconsistent (no solution possible).\n")
            
    return consistent


def plot_system(matrix=None):
    """Plots the lines and intersection point for a 2x3 linear system (2 equations, 2 variables).
    
    Parameters:
        matrix: 2x3 list of lists or numpy array (optional). If None, prompts interactively.
    """
    if matrix is None:
        matrix = _input_plot_system()
        
    mat = _normalize_matrix(matrix)
    if len(mat) != 2 or len(mat[0]) != 3:
        raise ValueError(
            f"plot_system requires a 2x3 augmented matrix (2 equations, 2 variables + constants). "
            f"Received shape: {len(mat)}x{len(mat[0])}"
        )
        
    orig_matrix = [row[:] for row in mat]
    REF(mat)
    REF_1(mat)
    RREF(mat)
    
    line_plot(mat, orig_matrix)


if __name__ == "__main__":
    main()