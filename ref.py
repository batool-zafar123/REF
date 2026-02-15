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
    # display(matrix)

    # matrix = [[1, 1, 1, 5],
    #           [1, 2, 0, 3],
    #           [2, 1, 3, 9],
    #           [2, 4, -5, 0]]
    # print(matrix)
    # REF(matrix, 4, 4)
    # print(matrix)


def REF(matrix, p, n):
    try:
        for i in range(p-1):
            for j in range(i, n-1):
                if not matrix[i][i] == 0:
                    mult = matrix[j+1][i]/matrix[i][i]
                    matrix[j+1] = [a - (mult)*b for a, b in zip(matrix[j+1], matrix[i])]
    except ZeroDivisionError:
        return

# Display function not completed yet...
# def display(matrix):
#     rows = len(matrix)
#     columns = len(matrix[0])
#     print("[", end = "")
#     for i in range(rows):
#         print("[", end = "")
#         for j in range(columns):
#             print(matrix[i][j], end = "  ")
#         print("]", end = "")
#         if not j == columns:
#             print()
#     print("]", end = "")


main()
