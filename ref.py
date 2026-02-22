def main():
    # INPUT from user--->
    # p = int(input("How many equations? "))
    # n = int(input("How many unknowns? "))
    # matrix = []
    # print()
    # for i in range(p):
    #     row = []
    #     for j in range(n):
    #         row.append(float(input(f"Enter entry # {i+1}{j+1}: ")))
    #     matrix.append(row)
    #     print()
    # display(matrix)

    matrix1 = [[6, 1, 1, 1, 0, 0],
               [4, -2, 5, 0, 1, 0],
               [2, 8, 7, 0, 0, 1]]
    
    # matrix2 = [[3, -1, 2, 5],
    #            [4, 0, 7, 2],
    #            [2, 1, -1, 3]]

    # matrix3 = [[1, 5, 8, 2],
    #            [-5, 3, 0, -7],
    #            [3, 4, 7, -1],
    #            [2, 1, 5, -3],
    #            [3, -8, 0, 3]]
    
    # matrix4 = [[1, 2, -1, -4],
    #            [2, 3, -1, -11],
    #            [-2, 0, -3, 22]]

    # matrix5 = [[4, 2, 3],
    #            [8, 4, 6],
    #            [12, 6, 9],
    #            [3, 2, 1]]
    

    display(matrix1)
    REF(matrix1, 3, 6)
    REF_1(matrix1, 3, 6)
    display(matrix1)
    RREF(matrix1, 3, 6)
    display(matrix1)

    # display(matrix2)
    # REF(matrix2, 3, 4)
    # REF_1(matrix2, 3, 4)
    # display(matrix2)

    # display(matrix3)
    # REF_(matrix3, 5, 4)
    # REF_1(matrix3, 5, 4)
    # display(matrix3)
    # RREF(matrix3, 5, 4)
    # display(matrix3)

    # display(matrix4)
    # REF(matrix4, 3, 3)
    # REF_1(matrix4, 3, 3)
    # display(matrix4)
    # RREF(matrix4, 3, 3)
    # display(matrix4)

    # display(matrix5)
    # REF(matrix5, 4, 3)
    # REF_1(matrix5, 4, 3)
    # display(matrix5)
    # RREF(matrix5, 4, 3)
    # display(matrix5)

    # matrix = [[1, 0, 0, -1],
    #           [0, 0, 0, 1],
    #           [0, 0, 0, 0]]
    
    # display(matrix)
    # REF(matrix, 3, 4)
    # REF_1(matrix, 3, 4)
    # display(matrix)
    # RREF(matrix, 3, 4)
    # display(matrix)



def REF_(matrix, p, n):
    try:
        for i in range(n):

            for j in range(i+1, p):

                mult = matrix[j][i] / matrix[i][i]

                matrix[j] = [a - mult * b for a, b in zip(matrix[j], matrix[i])]

            display(matrix)

    except ZeroDivisionError:
        print("Division with Zero!")
        return
    


def REF_1(matrix, p, n):
    if p > n:
        p = n
    for i in range(p):
        if not matrix[i][i] == 0:
            matrix[i] = [x / matrix[i][i] for x in matrix[i]]



def REF(matrix, rows, columns):
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



def RREF(matrix, p, n):
    
    for i in range(p-1, -1, -1):
        for k in range(n):
            if abs(matrix[i][k]) > 1e-9:
                pivot_column = k
                break

        for j in range(i-1, -1, -1):

            mult = matrix[j][pivot_column]
            matrix[j] = [a - mult * b for a, b in zip(matrix[j], matrix[i])]
                    


def display(matrix):
    r = len(matrix)
    c = len(matrix[0])
    zero_abs(matrix, r, c)
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



def zero_abs(matrix, r, c):
    for i in range(r):
        for j  in range(c):
            if matrix[i][j] == 0:
                matrix[i][j] = 0.0



main()