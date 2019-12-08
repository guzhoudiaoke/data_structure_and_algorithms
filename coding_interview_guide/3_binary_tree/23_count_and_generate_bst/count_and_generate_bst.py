import time
from functools import wraps


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, 'cost time:', end - start)
        return result
    return wrapper


@timethis
def num_bst(n):
    if n < 2:
        return 1

    dp = [0 for i in range(n+1)]
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]

    return dp[n]


@timethis
def num_bst2(n):
    def recursive(n):
        if n in d:
            return d[n]

        if n < 2:
            d[n] = 1
            return 1

        num = 0
        for i in range(1, n+1):
            num += recursive(i-1) * recursive(n-i)

        d[n] = num
        return num

    d = {}
    return recursive(n)


def generate(n):
    def clone_tree(root):
        if root is None:
            return None

        r = TreeNode(root.val)
        r.left = clone_tree(root.left)
        r.right = clone_tree(root.right)

        return r

    def recursive(start, end):
        res = []
        if start > end:
            return [None]

        root = None
        for i in range(start, end+1):
            root = TreeNode(i)
            left_subs = recursive(start, i-1)
            right_subs = recursive(i+1, end)
            for l in left_subs:
                for r in right_subs:
                    root.left, root.right = l, r
                    res.append(clone_tree(root))

        return res

    return recursive(1, n)


def print_tree_by_level(root):
    if root is None:
        return

    q = [root, None]
    level = 0
    print('level %d: ' % (level), end='')
    while q:
        node = q.pop(0)
        if node is None:
            if q:
                level += 1
                q.append(None)
                print()
                print('level %d: ' % (level), end='')
        else:
            print(node.val, end=', ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    print()
    print('------------------------')


def test(n):
    n1 = num_bst(n)
    n2 = num_bst2(n)
    print(n1, n2)


def test_generate(n):
    results = generate(n)
    for root in results:
        print_tree_by_level(root)


if __name__ == '__main__':
    test(3)
    test(8)
    test(13)
    test(33)
    test_generate(3)
