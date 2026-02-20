def main():
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

    matrix1 = [[1, 2, 3],
               [4, 2, 1],
               [1, 4, 3]]
    
    matrix2 = [[3, -1, 2, 5],
               [4, 0, 7, 2],
               [2, 1, -1, 3]]
    
    matrix3 = [[4, 2, 3],
               [-3, 0, 5],
               [0, 4, 6],
               [3, 2, 1]]
    

    # display(matrix1)
    # REF(matrix1, 3, 3)
    # display(matrix1)
    # REF_1(matrix1, 3, 3)
    # display(matrix1)

    # display(matrix2)
    # REF(matrix2, 3, 4)
    # display(matrix2)
    # REF_1(matrix2, 3, 4)
    # display(matrix2)

    # display(matrix3)
    # REF(matrix3, 4, 3)
    # display(matrix3)
    # REF_1(matrix3, 4, 3)
    # display(matrix3)
    REF_2(matrix1, 3, 3)
    REF_2(matrix2, 3, 4)
    REF_2(matrix3, 4, 3)

def REF(matrix, p, n):
    try:
        for i in range(n):

            for j in range(i+1, p):

                mult = matrix[j][i] / matrix[i][i]

                matrix[j] = [a - mult * b for a, b in zip(matrix[j], matrix[i])]

            # display(matrix)

    except ZeroDivisionError:
        print("Division with Zero!")
        return
    


def REF_1(matrix, p, n):
    if p > n:
        p = n
    for i in range(p):
        matrix[i] = [x / matrix[i][i] for x in matrix[i]]

def REF_2(matrix, rows, columns):
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
            # Eliminating enteries below pivot
            for j in range(pivot_row + 1, rows):
                mult = matrix[j][i] / pivot
                matrix[j] = [a - mult * b for a, b in zip(matrix[j], matrix[pivot_row])]
         
            pivot_row += 1
            if pivot_row == rows:
                break
    print(matrix)




# Display function not completed yet...
def display(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        print("[ ", end = "") if i == 0 else print("  ", end = "")
        for j in range(c):
            if not j == c-1:
                print(f"{matrix[i][j]:.4f}", "   ", end = "") 
            else:
                print(f"{matrix[i][j]:.4f}", "", end = "")
        print("]") if i == r-1 else print()
    print()
    



main()