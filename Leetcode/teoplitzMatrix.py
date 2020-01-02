matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

M = len(matrix)  # 3
N = len(matrix[0])  # 6

# how to travesal matrix with one variable
# for i in range(M * N):
#     print(matrix[i//N][i%N])


def isToeplitzMatrix(matrix) -> bool:
    M = len(matrix)
    N = len(matrix[0])
    for i in range(M - 1):
        for j in range(N - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True


matrix3 = [[1, 2, 3, 9], [5, 1, 2, 3], [1, 5, 1, 1]]
print(isToeplitzMatrix(matrix3))
