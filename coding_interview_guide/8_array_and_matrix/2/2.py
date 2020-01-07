def rotate(matrix):
    if matrix is None or len(matrix) == 0 or len(matrix[0]) != len(matrix):
        return

    size = len(matrix)
    for i in range(len(matrix)//2):
        matrix[i], matrix[size-i-1] = matrix[size-i-1], matrix[i]

    for i in range(size):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def test_rotate(size):
    n = 1
    mat = []
    for i in range(size):
        row = [n+j for j in range(size)]
        n += size
        mat.append(row)

    print(mat)
    rotate(mat)
    print(mat)


if __name__ == '__main__':
    test_rotate(3)
