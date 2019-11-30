import random
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, 'cost time:', end - start)
        return result
    return wrapper


@timethis
def get_num_of_sub_array(arr, num):
    ans = 0
    for i in range(len(arr)):
        for j in range (i, len(arr)):
            mmax = max(arr[i:j+1])
            mmin = min(arr[i:j+1])
            if mmax - mmin <= num:
                ans += 1

    return ans


@timethis
def get_num_of_sub_array2(arr, num):
    min_q = []
    max_q = []
    ans = 0

    j = 0
    for i in range(len(arr)):
        while j < len(arr):
            while len(min_q) and arr[min_q[-1]] >= arr[j]:
                min_q.pop()
            min_q.append(j)

            while len(max_q) and arr[max_q[-1]] <= arr[j]:
                max_q.pop()
            max_q.append(j)

            if arr[max_q[0]] - arr[min_q[0]] > num:
                break

            j += 1

        if min_q[0] == i:
            min_q.pop(0)

        if max_q[0] == i:
            max_q.pop(0)

        ans += j - i

    return ans


def test_get_num_of_sub_array(count, maxnum, delta):
    arr = []
    for _ in range(count):
        arr.append(random.randint(0, maxnum))

    num1 = get_num_of_sub_array(arr, delta)
    num2 = get_num_of_sub_array2(arr, delta)
    print(num1, num2)


if __name__ == '__main__':
    test_get_num_of_sub_array(10, 100, 10)
    test_get_num_of_sub_array(100, 1000, 100)
    test_get_num_of_sub_array(1000, 10000, 1000)
