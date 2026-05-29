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
        while pivot == 0:
            search_row += 1
            if search_row == rows:
                break  # No pivot found
            pivot = matrix[search_row][i]

        if search_row != pivot_row and search_row < rows:
            matrix[pivot_row], matrix[search_row] = matrix[search_row], matrix[pivot_row] 
        if pivot != 0:
            # Eliminating entries below pivot
            for j in range(pivot_row + 1, rows):
                mult = matrix[j][i] / pivot
                matrix[j] = [a - mult * b for a, b in zip(matrix[j], matrix[pivot_row])]
         
            pivot_row += 1
            if pivot_row == rows:
                break


def REF_1(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    pivot_row = 0
    for i in range(columns): 
        # Finding Pivot
        search_row = pivot_row
        pivot = matrix[pivot_row][i]
        while pivot == 0:
            search_row += 1
            if search_row == rows:
                break  # No pivot found
            pivot = matrix[search_row][i]

        if pivot != 0:
            matrix[pivot_row] = [x / pivot for x in matrix[pivot_row]]
        else:
            continue
        pivot_row += 1
        if pivot_row == rows:
            break


def RREF(matrix):
    p = len(matrix)
    n = len(matrix[0])
    
    for i in range(p-1, -1, -1):
        pivot_column = -1
        for k in range(n):
            if abs(matrix[i][k]) > 1e-9:
                pivot_column = k
                break
        if pivot_column == -1:
            continue

        for j in range(i-1, -1, -1):

            mult = matrix[j][pivot_column]
            matrix[j] = [a - mult * b for a, b in zip(matrix[j], matrix[i])]
                

def system(matrix):
    print("Original Matrix: ")
    display(matrix)
    plot_matrix = list(matrix)
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
                line_plot(plot_matrix, matrix) 
            else:
                pass
            
        else:
            print("The system has infinite many solutions. (Logic Pending)\n")
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


def line_plot(matrix, rref):
    x = np.linspace(rref[0][2] - 10, rref[0][2] + 10, 100)
    y1 = (matrix[0][2] - matrix[0][0] * x) / matrix[0][1]
    y2 = (matrix[1][2] - matrix[1][0] * x) / matrix[1][1]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label=f"y1 = {matrix[0][2] / matrix[0][1]} - {matrix[0][0] / matrix[0][1]}  x", color='blue') 
    plt.plot(x, y2, label=f"y2 = {matrix[1][2] / matrix[1][1]} - {matrix[1][0] / matrix[0][1]}  x", color='red')
    plt.grid(True, ls=":")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()


main()