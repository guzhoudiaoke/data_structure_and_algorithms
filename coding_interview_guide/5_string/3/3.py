def remove_k_zeros1(s, k):
    def remove(chars, start, count):
        while count:
            chars[start] = None
            start += 1
            count -= 1

    if s is None or k < 1:
        return s

    chars = list(s)
    start, count = -1, 0
    for i in range(len(chars)):
        if chars[i] == '0':
            count += 1
            start = i if start == -1 else start
        else:
            if count == k:
                remove(chars, start, count)
            start, count = -1, 0

    if count == k:
        remove(chars, start, count)

    return ''.join([c for c in chars if c])


def remove_k_zeros2(s, k):
    def remove(chars, start, count):
        while count:
            chars[start] = None
            start += 1
            count -= 1

    if s is None or k < 1:
        return s

    chars = list(s)
    first = 0
    while True:
        while first < len(chars) and chars[first] != '0':
            first += 1

        if first == len(chars):
            break

        last = first
        while last < len(chars) and chars[last] == '0':
            last += 1

        if last - first == k:
            remove(chars, first, k)

        first = last

    return ''.join([c for c in chars if c])


def test_remove_k_zeros():
    assert(remove_k_zeros1('', 2) == '')
    assert(remove_k_zeros2('', 2) == '')
    assert(remove_k_zeros1('A', 2) == 'A')
    assert(remove_k_zeros2('A', 2) == 'A')
    assert(remove_k_zeros1('A0', 2) == 'A0')
    assert(remove_k_zeros2('A0', 2) == 'A0')
    assert(remove_k_zeros1('A00B', 2) == 'AB')
    assert(remove_k_zeros2('A00B', 2) == 'AB')
    assert(remove_k_zeros1('A0000B000', 3) == 'A0000B')
    assert(remove_k_zeros2('A0000B000', 3) == 'A0000B')
    assert(remove_k_zeros1('A0000B000', 4) == 'AB000')
    assert(remove_k_zeros2('A0000B000', 4) == 'AB000')


if __name__ == '__main__':
    test_remove_k_zeros()
