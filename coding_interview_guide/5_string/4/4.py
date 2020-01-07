def is_rotation1(a, b):
    if a is None or b is None or len(a) != len(b):
        return False

    return a in b*2


def is_rotation2(a, b):
    return a and b and len(a) == len(b) and a in b*2


def test_is_rotation():
    assert(is_rotation1('cdab', 'abcd') is True)
    assert(is_rotation1('1ab2', 'ab12') is False)
    assert(is_rotation1('2ab1', 'ab12') is True)
    assert(is_rotation1('1234', '12341234') is False)

    assert(is_rotation2('cdab', 'abcd') is True)
    assert(is_rotation2('1ab2', 'ab12') is False)
    assert(is_rotation2('2ab1', 'ab12') is True)
    assert(is_rotation2('1234', '12341234') is False)


if __name__ == '__main__':
    test_is_rotation()
