import random


def max_lenght_of_sub_array_with_sum0(arr, k):
    if arr is None or len(arr) == 0 or k <= 0:
        return 0

    ans = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if k == sum(arr[i:j+1]):
                ans = max(ans, j-i+1)

    return ans


def max_lenght_of_sub_array_with_sum1(arr, k):
    if arr is None or len(arr) == 0 or k <= 0:
        return 0

    left, right = 0, 0
    current = arr[0]
    ans = 0

    while right < len(arr):
        if current == k:
            ans = max(ans, right-left+1)
            current -= arr[left]
            left += 1
        elif current < k:
            right += 1
            if right != len(arr):
                current += arr[right]
        else:
            current -= arr[left]
            left += 1

    return ans


def test(count, maxval):
    arr = [random.randint(1, maxval) for _ in range(count)]
    total = sum(arr)
    for k in range(total+1):
        ans0 = max_lenght_of_sub_array_with_sum0(arr, k)
        ans1 = max_lenght_of_sub_array_with_sum1(arr, k)
        assert(ans0 == ans1)


if __name__ == '__main__':
    test(10, 10)
    test(10, 100)
    test(100, 10)
