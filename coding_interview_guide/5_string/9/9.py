import random
import string


def search_string(arr, s):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        m = (left + right) // 2
        if arr[m] is not None:
            if arr[m] == s:
                result = m
                right = m - 1
            elif arr[m] < s:
                left = m + 1
            else:
                right = m - 1
        else:
            i = m
            while i >= left and arr[i] is None:
                i -= 1

            if i < left or arr[i] < s:
                left = m + 1
            elif arr[i] == s:
                result = i
                right = i - 1
            else:
                right = i - 1

    return result


def lower_bound(nums, target):
    begin = 0
    end = len(nums)

    while begin < end:
        mid = (begin + end) // 2
        if nums[mid] < target:
            begin = mid + 1
        else:
            end = mid

    return begin


def search_string2(arr, s):
    left = 0
    right = len(arr)

    while left < right:
        m = (left + right) // 2
        if arr[m] is not None:
            if arr[m] < s:
                left = m + 1
            else:
                right = m
        else:
            i = m
            while i >= left and arr[i] is None:
                i -= 1

            if i < left or arr[i] < s:
                left = m + 1
            else:
                right = i

    return left if left < len(arr) and arr[left] == s else -1


def test_search_string():
    arr = [None, None, 'a', None, None, 'b', 'c', None, 'd',
           None, None, 'e', 'f', 'g', None, 'h', None, 'i']

    print(search_string(arr, 'A'), search_string2(arr, 'A'))
    print(search_string(arr, 'a'), search_string2(arr, 'a'))
    print(search_string(arr, 'b'), search_string2(arr, 'b'))
    print(search_string(arr, 'c'), search_string2(arr, 'c'))
    print(search_string(arr, 'd'), search_string2(arr, 'd'))
    print(search_string(arr, 'e'), search_string2(arr, 'e'))
    print(search_string(arr, 'f'), search_string2(arr, 'f'))
    print(search_string(arr, 'g'), search_string2(arr, 'g'))
    print(search_string(arr, 'h'), search_string2(arr, 'h'))
    print(search_string(arr, 'i'), search_string2(arr, 'i'))
    print(search_string(arr, 'j'), search_string2(arr, 'j'))

    arr = []
    for i in range(100):
        size = random.randint(0, 26)
        s = ''.join(random.sample(string.ascii_letters+string.digits, size))
        arr.append(s)

    arr = sorted(arr)
    for i in range(100):
        arr.insert(random.randint(0, len(arr)), None)

    for i in range(len(arr)):
        s = arr[i]
        if s is None:
            size = random.randint(0, 26)
            s = ''.join(random.sample(string.ascii_letters, size))
            if s not in arr:
                assert(search_string2(arr, s) == search_string(arr, s))
        else:
            assert(search_string2(arr, s) == search_string(arr, s))

    print('pass')


if __name__ == '__main__':
    test_search_string()
