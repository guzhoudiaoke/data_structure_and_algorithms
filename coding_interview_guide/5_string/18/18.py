def max_unique_length(s):
    if s is None or len(s) == 0:
        return 0

    positions = {}
    pre = -1
    ans = 0
    for i, c in enumerate(s):
        pre = max(pre, positions.get(c, -1))
        ans = max(ans, i - pre)
        positions[c] = i

    return ans


def test_max_unique_length():
    assert(max_unique_length('abcd') == 4)
    assert(max_unique_length('aabcb') == 3)
    assert(max_unique_length('aaaaa') == 1)
    assert(max_unique_length('aabaa') == 2)
    assert(max_unique_length('acbbda') == 3)
    print('done')


if __name__ == '__main__':
    test_max_unique_length()
