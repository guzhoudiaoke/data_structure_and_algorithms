def num_sum(s):
    if s is None or len(s) == 0:
        return 0

    characters = [c for c in s]
    positive = True
    num = 0
    ans = 0

    for i in range(len(characters)):
        c = characters[i]
        n = ord(c) - ord('0')
        if n < 0 or n > 9:
            ans += num
            num = 0
            if c == '-':
                if i > 0 and characters[i-1] == '-':
                    positive = not positive
                else:
                    positive = False
            else:
                positive = True
        else:
            num = num*10 + n if positive else -n

    ans += num
    return ans


def num_sum2(s):
    if s is None or len(s) == 0:
        return 0

    characters = [c for c in s]
    positive = True
    num = 0
    ans = 0

    for i in range(len(characters)):
        c = characters[i]
        n = ord(c) - ord('0')
        if 0 <= n <= 9:
            num = num*10 + n if positive else -n
        else:
            if c == '-':
                prev = characters[i-1] if i > 0 else None
                positive = not positive if prev == '-' else False
            else:
                positive = True

            ans += num
            num = 0

    ans += num
    return ans


def test_num_sum():
    assert(num_sum('') == 0)
    assert(num_sum('A1.3') == 4)
    assert(num_sum('A-1B') == -1)
    assert(num_sum('A--1B') == 1)
    assert(num_sum('ACD-1XX--12B') == 11)
    assert(num_sum('A-1B--2C--D6E') == 7)

    assert(num_sum2('') == 0)
    assert(num_sum2('A1.3') == 4)
    assert(num_sum2('A-1B') == -1)
    assert(num_sum2('A--1B') == 1)
    assert(num_sum2('ACD-1XX--12B') == 11)
    assert(num_sum2('A-1B--2C--D6E') == 7)


if __name__ == '__main__':
    test_num_sum()
