import random


def max_length_of_sub_array_with_sum(arr, k):
    if arr is None or len(arr) == 0:
        return 0

    sum_map = {0: -1}
    current = 0
    ans = 0

    for i in range(len(arr)):
        current += arr[i]
        if current-k in sum_map:
            ans = max(ans, i-sum_map[current-k])
        if current not in sum_map:
            sum_map[current] = i

    return ans


def max_length_of_sub_array_with_sum2(arr, k):
    if arr is None or len(arr) == 0:
        return 0

    ans = 0
    for i in range(len(arr)):
        current = 0
        for j in range(i, len(arr)):
            current += arr[j]
            if current == k:
                ans = max(ans, j-i+1)

    return ans


def test(count, maxval):
    arr = [random.randint(-maxval, maxval) for _ in range(count)]
    total = abs(sum(arr))
    for k in range(-total, total+1):
        ans1 = max_length_of_sub_array_with_sum(arr, k)
        ans2 = max_length_of_sub_array_with_sum2(arr, k)
        assert(ans1 == ans2)


if __name__ == '__main__':
    test(10, 100)
    test(100, 100)
