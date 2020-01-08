from collections import defaultdict


def is_deformation(s1, s2):
    if s1 is None or s2 is None or len(s1) != len(s2):
        return False

    m = defaultdict(int)
    for c in s1:
        m[c] += 1

    for c in s2:
        if m[c] == 0:
            return False
        m[c] -= 1

    return True


def is_deformation2(s1, s2):
    if s1 is None or s2 is None or len(s1) != len(s2):
        return False

    m = [0] * 256
    for c in s1:
        m[ord(c)] += 1
    for c in s2:
        m[ord(c)] -= 1

    return max(m) == 0


def test_is_deformation():
    s1 = '123'
    s2 = '231'
    print(is_deformation(s1, s2))

    s1 = '123'
    s2 = '2331'
    print(is_deformation(s1, s2))

    assert(is_deformation('abcd', 'bcda') is True)
    assert(is_deformation('abd', 'bcda') is False)
    assert(is_deformation('aaa', 'aab') is False)
    assert(is_deformation('aba', 'aab') is True)

    assert(is_deformation2('abcd', 'bcda') is True)
    assert(is_deformation2('abd', 'bcda') is False)
    assert(is_deformation2('aaa', 'aab') is False)
    assert(is_deformation2('aba', 'aab') is True)


if __name__ == '__main__':
    test_is_deformation()
