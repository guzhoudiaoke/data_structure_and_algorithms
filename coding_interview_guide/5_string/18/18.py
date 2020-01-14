def max_unique_length(s):
    if s is None or len(s) == 0:
        return 0

    positions = {}
    pre = -1
    ans = 0
    for i, c in enumerate(s):
        if positions.get(c, -1) > pre:
            pre = positions.get(c, -1)
        if i - pre > ans:
            ans = i - pre
        positions[c] = i

    return ans


def test_max_unique_length():
    assert(max_unique_length('abcd') == 4)
    assert(max_unique_length('aabcb') == 3)
    assert(max_unique_length('aaaaa') == 1)
    assert(max_unique_length('aabaa') == 2)
    print('done')


if __name__ == '__main__':
    test_max_unique_length()
