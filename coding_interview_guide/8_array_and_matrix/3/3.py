def print_zig_zag1(mat):
    def do_print(beg_row, end_row, beg_col, end_col, down):
        if down:
            r, c = beg_row, beg_col
            while r <= end_row:
                result.append(mat[r][c])
                r += 1
                c -= 1
        else:
            r, c = end_row, end_col
            while r >= beg_row:
                result.append(mat[r][c])
                r -= 1
                c += 1

    if mat is None or len(mat) == 0 or len(mat[0]) == 0:
        return

    beg_row, end_row = 0, 0
    beg_col, end_col = 0, 0
    last_row, last_col = len(mat) - 1, len(mat[0]) - 1

    down = False
    result = []
    while beg_row < last_col+1:
        do_print(beg_row, end_row, beg_col, end_col, down)
        beg_row = beg_row+1 if beg_col == last_col else beg_row
        beg_col = beg_col if beg_col == last_col else beg_col+1
        end_col = end_col+1 if end_row == last_row else end_col
        end_row = end_row if end_row == last_row else end_row+1
        down = not down

    return result


def print_zig_zag2(mat):
    def do_print(beg_row, end_row, beg_col, end_col, down):
        if down:
            r, c = beg_row, beg_col
            while r <= end_row:
                result.append(mat[r][c])
                r += 1
                c -= 1
        else:
            r, c = end_row, end_col
            while r >= beg_row:
                result.append(mat[r][c])
                r -= 1
                c += 1

    if mat is None or len(mat) == 0 or len(mat[0]) == 0:
        return

    beg_row, end_row = 0, 0
    beg_col, end_col = 0, 0
    last_row, last_col = len(mat) - 1, len(mat[0]) - 1

    down = False
    result = []
    while beg_row < last_col+1:
        do_print(beg_row, end_row, beg_col, end_col, down)
        down = not down
        if beg_col != last_col:
            beg_col += 1
        else:
            beg_row += 1

        if end_row != last_row:
            end_row += 1
        else:
            end_col += 1

    return result


def print_zig_zag3(mat):
    if mat is None or len(mat) == 0 or len(mat[0]) == 0:
        return

    r, c = 0, 0
    last_row, last_col = len(mat) - 1, len(mat[0]) - 1
    result = []
    while True:
        # up-right
        while r >= 0 and c <= last_col:
            result.append(mat[r][c])
            if r == 0 or c == last_col:
                break
            r -= 1
            c += 1

        if r == last_row and c == last_col:
            break

        if c < last_col:
            c += 1
        else:
            r += 1

        # down-left
        while c >= 0 and r <= last_row:
            result.append(mat[r][c])
            if c == 0 or r == last_row:
                break
            r += 1
            c -= 1

        if r == last_row and c == last_col:
            break

        if r < last_row:
            r += 1
        else:
            c += 1

    return result


def test_print_zig_zag(row_num, col_num):
    n = 1
    mat = []
    for i in range(row_num):
        row = [n+j for j in range(col_num)]
        n += col_num
        mat.append(row)

    print(mat)
    result1 = print_zig_zag1(mat)
    result2 = print_zig_zag2(mat)
    result3 = print_zig_zag3(mat)
    print(result1)
    print(result2)
    print(result3)
    print('----------------------------')


if __name__ == '__main__':
    test_print_zig_zag(0, 0)
    test_print_zig_zag(0, 1)
    test_print_zig_zag(1, 0)
    test_print_zig_zag(3, 3)
    test_print_zig_zag(3, 4)
    test_print_zig_zag(4, 3)
    test_print_zig_zag(4, 4)
