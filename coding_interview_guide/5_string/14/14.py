def is_valid(s):
    if s is None or len(s) < 2 or len(s) % 2 != 0:
        return False

    count = 0
    for c in s:
        if c not in('(', ')'):
            return False
        if c == ')':
            count -= 1
            if count < 0:
                return False
        else:
            count += 1

    return count == 0


def max_valid_length(s):
    if s is None or len(s) == 0:
        return 0

    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')':
            prev = i - dp[i-1] - 1
            if prev >= 0 and s[prev] == '(':
                dp[i] = dp[i-1] + 2 + (dp[prev-1] if prev >= 1 else 0)

    return max(dp)


def test_is_valid():
    assert(is_valid('') is False)
    assert(is_valid('(') is False)
    assert(is_valid(')') is False)
    assert(is_valid('()') is True)
    assert(is_valid('()()') is True)
    assert(is_valid('(())') is True)
    assert(is_valid('(()())') is True)
    assert(is_valid(')((())') is False)
    assert(is_valid('())(') is False)
    print('pass')


def test_max_valid_length():
    assert(max_valid_length('(())') == 4)
    assert(max_valid_length('())') == 2)
    assert(max_valid_length('(()') == 2)
    assert(max_valid_length('(()())') == 6)
    assert(max_valid_length('()(()()(') == 4)
    print('pass')


if __name__ == '__main__':
    test_is_valid()
    test_max_valid_length()
