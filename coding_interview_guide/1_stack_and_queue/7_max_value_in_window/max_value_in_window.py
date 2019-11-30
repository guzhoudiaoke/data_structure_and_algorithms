import random
from collections import deque


def max_value_in_window(arr, window_size):
    dq = deque()
    result = []

    if arr is None or len(arr) < window_size or window_size < 1:
        return result

    for i in range(len(arr)):
        x = arr[i]
        while len(dq) != 0 and arr[dq[-1]] <= x:
            dq.pop()
        dq.append(i)

        if dq[0] == i - window_size:
            dq.popleft()

        if i >= window_size - 1:
            result.append(arr[dq[0]])

    return result


def test(count, maxnum, window_size):
    arr = []
    for _ in range(count):
        v = random.randint(0, maxnum)
        arr.append(v)

    result = max_value_in_window(arr, window_size)
    if len(result) != len(arr) - window_size + 1:
        raise Exception('Error result length')

    for i in range(len(result)):
        m = max(arr[i : i+window_size])
        if result[i] != m:
            raise Exception('Error result')


if __name__ == '__main__':
    test(100, 1000, 4)
    test(1000, 10000, 40)
    test(10000, 100000, 400)
    test(10000, 1000, 40)
