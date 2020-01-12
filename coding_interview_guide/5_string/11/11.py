def reverse(chars, beg, end):
    while beg < end:
        chars[beg], chars[end-1] = chars[end-1], chars[beg]
        beg += 1
        end -= 1


def rotate_by_word(s):
    if s is None:
        return s

    chars = list(s)
    reverse(chars, 0, len(chars))

    begin, end = -1, -1
    for i in range(len(chars)):
        c = chars[i]
        if c != ' ':
            if begin == -1:
                begin = i
        else:
            end = i

        if i == len(chars)-1:
            end = len(chars)

        if begin != -1 and end != -1:
            reverse(chars, begin, end)
            begin, end = -1, -1

    return ''.join(c for c in chars)


def rotate_by_word2(s):
    s = s[::-1]
    return ' '.join(a[::-1] for a in s.split())


def rotate_k(s, k):
    if s is None or len(s) < k:
        return s

    chars = list(s)
    reverse(chars, 0, k)
    reverse(chars, k, len(chars))
    reverse(chars, 0, len(chars))

    return ''.join(c for c in chars)


def rotate_k2(s, k):
    return s[k:] + s[:k]


def rotate_k3(s, k):
    def exchange(chars, begin, end, size):
        i = end - size
        for _ in range(size):
            chars[begin], chars[i] = chars[i], chars[begin]
            begin += 1
            i += 1

    if s is None or len(s) < k:
        return s

    chars = list(s)
    begin, end = 0, len(s)
    left, right = k, len(s)-k

    while True:
        d = left - right
        s = min(left, right)
        exchange(chars, begin, end, s)

        if d == 0:
            break
        elif d < 0:
            end -= s
            right = -d
        elif d > 0:
            begin += s
            left = d

    return ''.join(chars)


def test_reverse():
    s = 'abcdef'
    chars = list(s)
    reverse(chars, 0, len(chars))
    r = ''.join(chars)
    r1 = s[::-1]
    r2 = ''.join(reversed(s))
    assert(r == r1)
    assert(r == r2)
    print('test reverse done')


def test_rotate_by_word():
    assert(rotate_by_word('abc def') == 'def abc')
    assert(rotate_by_word('dog loves pig') == 'pig loves dog')
    assert(rotate_by_word("I'm a student.") == "student. a I'm")
    assert(rotate_by_word2('abc def') == 'def abc')
    assert(rotate_by_word2('dog loves pig') == 'pig loves dog')
    assert(rotate_by_word2("I'm a student.") == "student. a I'm")
    print('test rotate by word done')


def test_rotate_k():
    assert(rotate_k('abcde', 3) == 'deabc')
    assert(rotate_k2('abcde', 3) == 'deabc')
    assert(rotate_k3('1234567ABCD', 7) == 'ABCD1234567')
    print('test rotate k done')


if __name__ == '__main__':
    test_reverse()
    test_rotate_k()
    test_rotate_by_word()
