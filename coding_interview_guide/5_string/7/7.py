def count_string(s):
    if s is None or len(s) == 0:
        return s

    beg, end = 0, 0
    ret = ''
    while beg < len(s):
        end = beg
        while end < len(s) and s[end] == s[beg]:
            end += 1
        ret += s[beg] + '_' + str(end-beg)
        if end != len(s):
            ret += '_'
        beg = end

    return ret


def get_char(cs, index):
    beg = 0
    index += 1
    while index >= 0:
        c = cs[beg]
        beg += 2
        i = beg
        while i < len(cs) and cs[i].isdigit():
            i += 1

        num = int(cs[beg:i])
        if index <= num:
            return c

        beg = i+1
        index -= num

    return None


def test_count_string():
    assert(count_string('aaabbadddffc') == 'a_3_b_2_a_1_d_3_f_2_c_1')
    assert(count_string('aaabbbbbbbbcde') == 'a_3_b_8_c_1_d_1_e_1')

    s = 'aaabbadddffc'
    cs = count_string(s)
    for i in range(len(s)):
        print(i, s[i], get_char(cs, i))
        assert(s[i] == get_char(cs, i))

    s = 'a'*1 + 'b'*11 + 'c'*111
    cs = count_string(s)
    for i in range(len(s)):
        print(i, s[i], get_char(cs, i))
        assert(s[i] == get_char(cs, i))
    print('done')


if __name__ == '__main__':
    test_count_string()
