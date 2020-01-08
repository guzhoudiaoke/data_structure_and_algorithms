def replace(s, f, t):
    def clear(chars, beg, end):
        for i in range(beg, end+1):
            chars[i] = None

    if s is None or f is None or t is None:
        return s
    if len(s) == 0 or len(f) == 0:
        return s

    chars_s = list(s)
    chars_f = list(f)
    index = 0
    for i in range(len(chars_s)):
        c = chars_s[i]
        if c == chars_f[index]:
            index += 1
            if index == len(f):
                clear(chars_s, i-index+1, i)
                index = 0
        else:
            index = 0

    ret = ''
    i = 0
    while i < len(chars_s):
        c = chars_s[i]
        if c is not None:
            ret += c
            i += 1
        else:
            while i < len(chars_s):
                c = chars_s[i]
                if c is not None:
                    break
                i += 1
            ret += t

    return ret


def test_replace():
    assert(replace('123abc', 'abc', '4567') == '1234567')
    assert(replace('123abcabc', 'abc', '4567') == '1234567')
    assert(replace('123', 'abc', '4567') == '123')
    assert(replace('123abcabcd', 'abc', '4567') == '1234567d')
    print('done')


if __name__ == '__main__':
    test_replace()
