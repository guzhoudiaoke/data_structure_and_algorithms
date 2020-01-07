def cycle_print1(matrix):
    def recursive(matrix, row_beg, row_end, col_beg, col_end):
        if row_beg > row_end or col_beg > col_end:
            return

        if row_beg == row_end:
            for c in range(col_beg, col_end+1):
                result.append(matrix[row_beg][c])
        elif col_beg == col_end:
            for r in range(row_beg, row_end+1):
                result.append(matrix[r][col_beg])
        else:
            for c in range(col_beg, col_end+1):
                result.append(matrix[row_beg][c])

            for r in range(row_beg+1, row_end+1):
                result.append(matrix[r][col_end])

            for c in range(col_end-1, col_beg-1, -1):
                result.append(matrix[row_end][c])

            for r in range(row_end-1, row_beg, -1):
                result.append(matrix[r][col_beg])

            recursive(matrix, row_beg+1, row_end-1, col_beg+1, col_end-1)

    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return

    print(matrix)
    result = []
    recursive(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1)
    return result


def cycle_print2(matrix):
    def cycle(matrix, row_beg, row_end, col_beg, col_end):
        if row_beg > row_end or col_beg > col_end:
            return

        if row_beg == row_end:
            for c in range(col_beg, col_end+1):
                result.append(matrix[row_beg][c])
        elif col_beg == col_end:
            for r in range(row_beg, row_end+1):
                result.append(matrix[r][col_beg])
        else:
            for c in range(col_beg, col_end+1):
                result.append(matrix[row_beg][c])

            for r in range(row_beg+1, row_end+1):
                result.append(matrix[r][col_end])

            for c in range(col_end-1, col_beg-1, -1):
                result.append(matrix[row_end][c])

            for r in range(row_end-1, row_beg, -1):
                result.append(matrix[r][col_beg])

    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return

    print(matrix)
    result = []

    row_beg, row_end = 0, len(matrix)-1
    col_beg, col_end = 0, len(matrix[0])-1
    while row_beg <= row_end and col_beg <= col_end:
        cycle(matrix, row_beg, row_end, col_beg, col_end)
        row_beg += 1
        row_end -= 1
        col_beg += 1
        col_end -= 1
    return result


def test_cycle_print(row_num, col_num):
    mat = []
    n = 1
    for _ in range(row_num):
        row = [n+i for i in range(col_num)]
        n += col_num
        mat.append(row)

    result1 = cycle_print1(mat)
    result2 = cycle_print2(mat)
    print(result1)
    print(result2)
    print('----------------------------------------------------')


if __name__ == '__main__':
    test_cycle_print(0, 0)
    test_cycle_print(0, 1)
    test_cycle_print(1, 0)
    test_cycle_print(1, 1)
    test_cycle_print(1, 2)
    test_cycle_print(2, 1)
    test_cycle_print(2, 2)
    test_cycle_print(4, 4)
    test_cycle_print(4, 3)
    test_cycle_print(3, 4)
    test_cycle_print(6, 6)
    test_cycle_print(6, 4)
    test_cycle_print(4, 6)
