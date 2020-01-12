import random
import string
import re


def replace(s):
    chars = list(s)
    n = chars.count(' ')
    chars += [None] * n * 2

    right = len(chars) - 1
    left = len(s) - 1
    while left >= 0:
        if chars[left] == ' ':
            chars[right-2], chars[right-1], chars[right] = '%', '2', '0'
            right -= 3
        else:
            chars[right] = chars[left]
            right -= 1
        left -= 1

    return ''.join(chars)


def modify(s):
    chars = list(s)
    left = len(s) - 1
    right = left

    while left >= 0:
        if chars[left] != '*':
            chars[right] = chars[left]
            right -= 1
        left -= 1

    while right >= 0:
        chars[right] = '*'
        right -= 1

    return ''.join(chars)


def test_replace():
    for _ in range(100):
        size = random.randint(0, 36)
        chars = random.sample(string.ascii_letters + string.digits, size)
        for __ in range(size):
            pos = random.randint(0, len(chars))
            chars = chars[:pos] + [' '] + chars[pos:]

        s = ''.join(chars)
        result1 = replace(s)
        result2 = re.sub(r' ', '%20', s)
        result3 = s.replace(' ', '%20')
        assert(result1 == result2)
        assert(result2 == result3)

    print('done')


def test_modify():
    for _ in range(100):
        size = random.randint(0, 100)
        chars = []
        for __ in range(size):
            chars += random.choice(string.digits)
        for __ in range(size):
            pos = random.randint(0, len(chars))
            chars = chars[:pos] + ['*'] + chars[pos:]

        s = ''.join(chars)
        result = modify(s)
        assert(s.count('*') == result.count('*'))
        assert(s.replace('*', '') == result.replace('*', ''))

    print('done')


if __name__ == '__main__':
    test_replace()
    test_modify()
