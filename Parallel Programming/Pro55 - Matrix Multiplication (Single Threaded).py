
matrix_size = 3
matrix_1 = [[4, 3, 5], [-1, 2, 0], [-6, 7, 9]]
matrix_2 = [[8, 2, 1], [7, 5, 4], [6, -7, -8]]

result_matrix = [[0] * matrix_size for i in range(matrix_size)]

for row in range (matrix_size):
    for column in range(matrix_size):
        for d in range(matrix_size):
            result_matrix[row][column] += matrix_1[row][d] * matrix_2[d][column]

'''
print(result_matrix)
'''

for i in range(matrix_size):
    print(matrix_1[i], matrix_2[i], result_matrix[i])
print("...")
