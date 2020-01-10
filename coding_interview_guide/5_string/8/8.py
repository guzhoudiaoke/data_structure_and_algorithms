import random
import string


def is_unique(s):
    if s is None:
        return True

    char_map = {}
    for c in s:
        if c in char_map:
            return False
        char_map[c] = True

    return True


def is_unique2(s):
    if s is None:
        return True

    sorted_s = sorted(s)
    for i in range(1, len(sorted_s)):
        if sorted_s[i] == sorted_s[i-1]:
            return False

    return True


def heap_sort(arr):
    def left(index):
        return index*2 + 1

    def right(index):
        return index*2 + 2

    def heapify(arr, index, size):
        left_child = left(index)
        right_child = right(index)

        largest = index
        if left_child < size and arr[left_child] > arr[largest]:
            largest = left_child
        if right_child < size and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            heapify(arr, largest, size)

    def build_heap(arr):
        for i in range(len(arr)//2, -1, -1):
            heapify(arr, i, len(arr))

    build_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


def is_unique3(s):
    if s is None:
        return True

    chars = list(s)
    heap_sort(chars)
    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            return False

    return True


def is_unique4(s):
    if s is None:
        return True

    return len(set(s)) == len(s)


def test_heap_sort(count):
    arr = [i for i in range(count)]
    random.shuffle(arr)
    heap_sort(arr)
    assert(sorted(arr) == arr)


def test_is_unique():
    assert(is_unique('') is True)
    assert(is_unique('a') is True)
    assert(is_unique('ab') is True)
    assert(is_unique('abcd') is True)
    assert(is_unique('aa') is False)
    assert(is_unique('aba') is False)
    assert(is_unique('abbcde') is False)

    assert(is_unique2('') is True)
    assert(is_unique2('a') is True)
    assert(is_unique2('ab') is True)
    assert(is_unique2('abcd') is True)
    assert(is_unique2('aa') is False)
    assert(is_unique2('aba') is False)
    assert(is_unique2('abbcde') is False)

    assert(is_unique3('') is True)
    assert(is_unique3('a') is True)
    assert(is_unique3('ab') is True)
    assert(is_unique3('abcd') is True)
    assert(is_unique3('aa') is False)
    assert(is_unique3('aba') is False)
    assert(is_unique3('abbcde') is False)

    for i in range(100):
        size = random.randint(0, 26)
        s = ''.join(random.sample(string.ascii_letters+string.digits, size))
        assert(is_unique(s) == is_unique2(s))
        assert(is_unique2(s) == is_unique3(s))
        assert(is_unique3(s) == is_unique4(s))

    print('done')


if __name__ == '__main__':
    test_heap_sort(5)
    test_heap_sort(50)
    test_heap_sort(500)
    test_is_unique()
