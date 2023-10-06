def matrix_func(mat):
    try:
        no_zero_col = 0
        for j in range(0, len(mat[0])):
            contains_zero = False
            for i in range(0, len(mat)):
                if (mat[i][j] == 0):
                    contains_zero = True
            if (not contains_zero):
                no_zero_col += 1
        return no_zero_col
    except Exception:
        print('Произошла ошибка!')
        return 0

print('Количество столбцов, не содержащих ни одного нулевого элемента')
print(matrix_func([[1,2,3,4,5],
                   [1,0,3,0,5],
                   [1,0,3,0,5]]))
