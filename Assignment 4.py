#Q4
matrix_1 = [[1, 4],
            [5, 3]]

matrix_2 = [[4, 2],
            [7, 0]]

addition = []

for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[i])):
        row.append(matrix_1[i][j] + matrix_2[i][j])
    addition.append(row)

print("Matrix Addition:")
for row in addition:
    print(row)