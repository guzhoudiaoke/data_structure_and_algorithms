import random


def max_area_of_histogram0(heights):
    max_area = 0
    for i in range(len(heights)):
        h = heights[i]
        l, r = i, i
        while l >= 0 and heights[l] >= h:
            l -= 1
        while r < len(heights) and heights[r] >= h:
            r += 1

        max_area = max(max_area, h * (r - l - 1))
    return max_area


def max_area_of_histogram(heights):
    max_area = 0
    stack = []
    for i in range(len(heights)):
        while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
            top = stack.pop()
            w = i if len(stack) == 0 else i - stack[-1] - 1
            cur_area = heights[top] * w
            max_area = max(max_area, cur_area)
        stack.append(i)

    n = len(heights)
    while len(stack) > 0:
        top = stack.pop()
        w = n if len(stack) == 0 else n - stack[-1] - 1
        cur_area = w * heights[top]
        max_area = max(max_area, cur_area)

    return max_area


def max_area_of_histogram2(heights):
    max_area = 0
    stack = []
    for i in range(len(heights) + 1):
        h = heights[i] if i < len(heights) else -1
        while len(stack) > 0 and heights[stack[-1]] >= h:
            top = stack.pop()
            l = -1 if len(stack) == 0 else stack[-1]
            cur_area = (i - l - 1) * heights[top]
            max_area = max(max_area, cur_area)
        stack.append(i)

    return max_area


def max_area_of_histogram3(heights):
    max_area = 0
    stack = []
    heights.append(0)
    for i in range(len(heights)):
        h = heights[i]
        while len(stack) > 0 and heights[stack[-1]] >= h:
            top = stack.pop()
            l = -1 if len(stack) == 0 else stack[-1]
            cur_area = (i - l - 1) * heights[top]
            max_area = max(max_area, cur_area)
        stack.append(i)

    heights.pop()
    return max_area


def max_area_of_histogram4(heights):
    max_area = 0
    stack = []
    heights.append(0)
    for i in range(len(heights)):
        h = heights[i]
        while len(stack) > 0 and heights[stack[-1]] > h:
            top = stack.pop()
            l = -1 if len(stack) == 0 else stack[-1]
            cur_area = (i - l - 1) * heights[top]
            max_area = max(max_area, cur_area)
        stack.append(i)

    heights.pop()
    return max_area
def max_sub_matrix_size(matrix):
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    r, c = len(matrix), len(matrix[0])
    max_area = 0
    heights = [ 0 for _ in range(c) ]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                heights[j] = heights[j] + 1
            else:
                heights[j] = 0
        max_area = max(max_area, max_area_of_histogram3(heights))

    return max_area


def test_max_area_of_histogram(count, minnum, maxnum):
    heights = []
    for i in range(count):
        a = random.randint(minnum, maxnum)
        heights.append(a)

    area0 = max_area_of_histogram0(heights)
    area1 = max_area_of_histogram(heights)
    area2 = max_area_of_histogram2(heights)
    area3 = max_area_of_histogram3(heights)
    area4 = max_area_of_histogram4(heights)
    if area0 != area1:
        raise Exception('Error 0', area0, area1)
    if area1 != area2:
        raise Exception('Error 1', area1, area2)
    if area2 != area3:
        raise Exception('Error 2', area2, area3)
    if area3 != area4:
        raise Exception('Error 3', area3, area4)


def test_max_sub_matrix_size(r, c, percentage):
    matrix = []
    for _ in range(r):
        row = []
        for _ in range(c):
            a = random.randint(0, 100)
            if a < percentage:
                row.append(0)
            else:
                row.append(1)
        matrix.append(row)

    ans = max_sub_matrix_size(matrix)
    for i in range(r):
        print(matrix[i])
    print(ans)


if __name__ == '__main__':
    test_max_area_of_histogram(10, 1, 100)
    test_max_area_of_histogram(100, 1, 100)
    test_max_area_of_histogram(1000, 1, 100)
    test_max_area_of_histogram(10000, 1, 100)
    test_max_area_of_histogram(100000, 1, 100)
    
    test_max_sub_matrix_size(10, 10, 60)
    test_max_sub_matrix_size(10, 10, 30)
    test_max_sub_matrix_size(10, 10, 10)

