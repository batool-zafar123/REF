matrix = [[1, 2, 3], [6, 8, 2], [1, 0, 1]]
i = 0
j = 0
n = 3

# working fine for first column
for j in range(1):
    i = 0
    pivot = matrix[i][j] # set the pivot
    pivot_row = i
    while pivot == 0 and i != n: # if it's 0 then 
        i = i + 1 # move to the next row
        pivot_row = i
        pivot = matrix[i][j] # set the element as pivot 
    if i==n:
        continue
    if pivot != 1:
        for _ in matrix[i]: # for each element in the row.
            matrix[i][j] = matrix[i][j] / pivot # divide it by the pivot
    i = i + 1 # move to the next row
    if i == n:
        continue
    while matrix[i][j] == 0 and i != n: # while the element is not zero.
        i = i + 1
    if i==n:
        continue
    while i < n:
        if matrix[i][j] != 0:
            for j in range(n):
                matrix[i][j] = matrix[i][j] - (matrix[i][j] * matrix[pivot_row][j])
        i = i + 1
        j = 0

print(matrix)

