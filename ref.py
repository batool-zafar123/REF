# matrix = [[1, 2, 3], [6, 8, 2], [1, 0, 1]]
# i = 0
# j = 0
# n = 3

# # working fine for first column
# for j in range(1):
#     i = 0
#     pivot = matrix[i][j] # set the pivot
#     pivot_row = i
#     while pivot == 0 and i != n: # if it's 0 then 
#         i = i + 1 # move to the next row
#         pivot_row = i
#         pivot = matrix[i][j] # set the element as pivot 
#     if i==n:
#         continue
#     if pivot != 1:
#         for _ in matrix[i]: # for each element in the row.
#             matrix[i][j] = matrix[i][j] / pivot # divide it by the pivot
#     i = i + 1 # move to the next row
#     if i == n:
#         continue
#     while matrix[i][j] == 0 and i != n: # while the element is not zero.
#         i = i + 1
#     if i==n:
#         continue
#     while i < n:
#         if matrix[i][j] != 0:
#             for j in range(n):
#                 matrix[i][j] = matrix[i][j] - (matrix[i][j] * matrix[pivot_row][j])
#         i = i + 1
#         j = 0

# print(matrix)


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

    display(matrix1)
    REF(matrix1, 3, 3)
    display(matrix1)
    REF_1(matrix1, 3, 3)
    display(matrix1)

    display(matrix2)
    REF(matrix2, 3, 4)
    display(matrix2)
    REF_1(matrix2, 3, 4)
    display(matrix2)

    display(matrix3)
    REF(matrix3, 4, 3)
    display(matrix3)
    REF_1(matrix3, 4, 3)
    display(matrix3)



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