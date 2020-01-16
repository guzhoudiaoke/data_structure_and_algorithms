def point_new_char(s, index):
    if s is None or index >= len(s):
        return None

    k = index - 1
    count = 0
    while k > 0 and s[k].isupper():
        k -= 1
        count += 1

    if count % 2 == 1:
        return s[index-1: index+1]
    else:
        if s[index].islower():
            return s[index]
        else:
            return s[index: index+2]


def test_point_new_char():
    s = 'aaABCDEcBCg'
    assert(point_new_char(s, 7) == 'Ec')
    assert(point_new_char(s, 4) == 'CD')
    assert(point_new_char(s, 10) == 'g')
    print('pass')


if __name__ == '__main__':
    test_point_new_char()
