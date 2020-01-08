def check(s):
    if s is None or len(s) == 0:
        return False
    if not s[0].isdigit() and s[0] != '-':
        return False
    if s[0] == '-' and (len(s) == 1 or s[1] == '0'):
        return False
    if s[0] == '0' and len(s) != 1:
        return False

    for c in s[1:]:
        if not c.isdigit():
            return False

    return True


def convert(s):
    if not check(s):
        return 0

    num = 0
    positive, i = (True, 0) if s[0] != '-' else (False, 1)
    overflow = 0x80000000
    for c in s[i:]:
        a = ord(c) - ord('0')
        if (num > overflow//10) or (num == overflow//10 and a > overflow % 10):
            return 0

        num = num*10 + a

    if num == overflow and positive:
        return 0

    return num if positive else -num


def test_convert():
    assert(convert('') == 0)
    assert(convert('-') == 0)
    assert(convert('-0') == 0)
    assert(convert('--') == 0)
    assert(convert('-012') == 0)
    assert(convert('-x') == 0)
    assert(convert('x') == 0)
    assert(convert('123x') == 0)
    assert(convert('0123') == 0)

    assert(convert('0') == 0)
    assert(convert('123') == 123)
    assert(convert('-123') == -123)
    assert(convert('2147483647') == 2147483647)
    assert(convert('2147483648') == 0)
    assert(convert('-2147483648') == -2147483648)

    print('done')


if __name__ == '__main__':
    test_convert()
