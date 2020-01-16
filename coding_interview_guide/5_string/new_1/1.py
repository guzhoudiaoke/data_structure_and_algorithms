import functools


def cmp_str(a, b):
    if a+b < b+a:
        return -1
    if a+b > b+a:
        return 1
    return 0


def solve(strs):
    strs = sorted(strs, key=functools.cmp_to_key(cmp_str))
    print(''.join(strs))


n = int(input())
strs = []
for _ in range(n):
    strs.append(input())

solve(strs)
