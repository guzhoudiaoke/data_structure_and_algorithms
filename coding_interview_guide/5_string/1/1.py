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


if __name__ == '__main__':
    test_is_deformation()
