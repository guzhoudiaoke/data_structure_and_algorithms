def is_contain(matrix, k):
    if matrix is None or matrix[0] is None:
        return False

    r = 0
    c = len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        if matrix[r][c] == k:
            return True
        if matrix[r][c] > k:
            c -= 1
        else:
            r += 1

    return False


def test_is_contain():
    matrix = [[0, 1, 2, 5], [2, 3, 4, 7],
              [4, 4, 4, 8], [5, 7, 7, 9]]
    for i in range(10):
        print(i, is_contain(matrix, i))


if __name__ == '__main__':
    test_is_contain()
