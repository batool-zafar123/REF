def main():

    # matrix = matrix_input()
    
    matrix1 = [[6, 1, 1, 1, 0, 0],
               [4, -2, 5, 0, 1, 0],
               [2, 8, 7, 0, 0, 1]]
    
    system(matrix1)
    
    matrix2 = [[3, -1, 2, 5],
               [4, 0, 7, 2],
               [2, 1, -1, 3]]
    
    system(matrix2)

    matrix3 = [[1, 5, 8, 2],
               [-5, 3, 0, -7],
               [3, 4, 7, -1],
               [2, 1, 5, -3],
               [3, -8, 0, 3]]
    
    system(matrix3)
    
    matrix4 = [[1, 2, -1, -4],
               [2, 3, -1, -11],
               [-2, 0, -3, 22]]
    
    system(matrix4)

    matrix5 = [[4, 2, 3],
               [8, 4, 6],
               [12, 6, 9],
               [3, 2, 1]]
    
    system(matrix5)

    matrix6 = [[1, 2, -1, 1, 1, 3, -6],
               [2, 5, -1, 2, 2, 7, -13],
               [-1, 1, 4, -2, 1, -1, 11],
               [3, -1, 2, 5, -2, 1, 0],
               [1, 0, 1, 0, 4, -2, 19],
               [0, 2, -3, 1, 1, 5, -15]]
    
    system(matrix6)
    
    matrix7 = []

    system(matrix7)


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
            print()
        else:
            print("The system has infinite many solutions. (Logic Pending)\n")
    else:
        print("System is inconsistent. Solution not possible.\n")


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
    n = int(input("How many unknowns? "))
    matrix = []
    print()
    for i in range(p):
        row = []
        for j in range(n):
            row.append(float(input(f"Enter entry # {i+1}{j+1}: ")))
        matrix.append(row)
        print()
    return matrix



main()