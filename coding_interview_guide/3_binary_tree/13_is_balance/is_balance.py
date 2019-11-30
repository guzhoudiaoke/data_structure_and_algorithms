import random
import operator


class TreeNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def __eq__(self, rhs):
        def recursive(lhs, rhs):
            if lhs is None:
                return rhs is None

            if rhs is None:
                return lhs is None

            if lhs.key != rhs.key or lhs.val != rhs.val:
                return False

            if not recursive(lhs.left, rhs.left):
                return False

            if not recursive(lhs.left, rhs.left):
                return False

            return True

        return recursive(self.root, rhs.root)

    def insert_recursive(self, key, val):
        def recursive(node, key, val):
            if not node:
                return TreeNode(key, val)

            if key < node.key:
                node.left = recursive(node.left, key, val)
            elif key > node.key:
                node.right = recursive(node.right, key, val)

            return node

        self.root = recursive(self.root, key, val)

    def insert_non_recursive(self, key, val):
        node = TreeNode(key, val)
        if not self.root:
            self.root = node
            return

        parent = None
        cur = self.root
        while cur:
            parent = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                cur.val = val
                return

        if key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def inorder_traversal_recursive(self):
        def recursive(node):
            if node:
                recursive(node.left)
                result.append(node.key)
                recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def inorder_traversal_non_recursive(self):
        result = []
        if not self.root:
            return result

        node = self.root
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.key)
                node = node.right

        return result

    def preorder_traversal_recursive(self):
        def recursive(node):
            if node:
                result.append(node.key)
                recursive(node.left)
                recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def preorder_traversal_non_recursive(self):
        result = []
        if not self.root:
            return result

        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.key)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def postorder_traversal_recursive(self):
        def recursive(node):
            if node:
                recursive(node.left)
                recursive(node.right)
                result.append(node.key)

        result = []
        recursive(self.root)
        return result

    def postorder_traversal_non_recursive1(self):
        result = []
        if not self.root:
            return result

        stack1 = [self.root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            result.append(stack2.pop().key)

        return result

    def postorder_traversal_non_recursive2(self):
        result = []
        if not self.root:
            return result

        stack = [self.root]
        flag = self.root
        while stack:
            node = stack[-1]
            if node.left and node.left != flag and node.right != flag:
                stack.append(node.left)
            elif node.right and node.right != flag:
                stack.append(node.right)
            else:
                result.append(stack.pop().key)
                flag = node

        return result

    def height(self):
        def recursive(node):
            if node is None:
                return 0

            hl = recursive(node.left)
            hr = recursive(node.right)
            return max(hl, hr) + 1

        return recursive(self.root)

    def print_by_level1(self):
        if self.root is None:
            return

        q = [(self.root, 1)]
        level = 0
        while q:
            node, lv = q.pop(0)
            if lv != level:
                level = lv
                print()
                print('level', lv, ': ', end='')

            print(node.key, end=', ')
            if node.left:
                q.append((node.left, lv+1))
            if node.right:
                q.append((node.right, lv+1))

        print()

    def print_by_level(self):
        if self.root is None:
            return

        q = [self.root, None]
        level = 0
        print('level', level, ': ', end='')
        while q:
            node = q.pop(0)
            if node is None:
                if q:
                    level += 1
                    q.append(None)
                    print()
                    print('level', level, ': ', end='')
            else:
                print(node.key, end=', ')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        print()

    def print_zigzag1(self):
        if self.root is None:
            return

        q = [None, self.root]
        level = 0
        print('level', level, ': ', end='')
        while q:
            if level % 2 == 1:
                node = q.pop(0)
            else:
                node = q.pop(-1)

            if node is None:
                print()
                if q:
                    level += 1
                    if level % 2 == 1:
                        q.append(None)
                    else:
                        q.insert(0, None)
                    print('level', level, ': ', end='')
            else:
                print(node.key, end=', ')
                if level % 2 == 1:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    if node.right:
                        q.insert(0, node.right)
                    if node.left:
                        q.insert(0, node.left)

    def print_zigzag(self):
        def get_next():
            if level % 2 == 0:
                return q.pop(0)
            else:
                return q.pop(-1)

        def add_children(node):
            if level % 2 == 0:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if node.right:
                    q.insert(0, node.right)
                if node.left:
                    q.insert(0, node.left)

        def add_level_flag():
            if level % 2 == 0:
                q.append(None)
            else:
                q.insert(0, None)

        if self.root is None:
            return

        q = [self.root, None]
        level = 0
        print('level', level, ': ', end='')
        while q:
            node = get_next()
            if node is None:
                print()
                if q:
                    level += 1
                    add_level_flag()
                    print('level', level, ': ', end='')
            else:
                print(node.key, end=', ')
                add_children(node)

    def is_balance1(self):
        def height(node):
            if node is None:
                return 0

            l = height(node.left)
            r = height(node.right)
            return max(l, r) + 1

        def balance(node):
            if node is None:
                return True

            l_height = height(node.left)
            r_height = height(node.right)
            if abs(l_height - r_height) > 1:
                return False

            left_balance = balance(node.left)
            right_balance = balance(node.right)
            return left_balance and right_balance
        
        return balance(self.root)

    def is_balance2(self):
        def get_height(node):
            if node is None:
                return 0

            left_height = get_height(node.left)
            if not balance[0]:
                return left_height + 1

            right_height = get_height(node.right)
            if not balance[0]:
                return right_height + 1

            if abs(left_height - right_height) > 1:
                balance[0] = False

            return max(left_height, right_height) + 1

        balance = [True]
        get_height(self.root)
        return balance[0]

    def is_balance(self):
        def get_height(node):
            if node is None:
                return 0, True

            left_height, left_balance = get_height(node.left)
            if not left_balance:
                return 0, False

            right_height, right_balance = get_height(node.right)
            if not right_balance:
                return 0, False

            if abs(left_height - right_height) > 1:
                return max(left_height, right_height) + 1, False

            return max(left_height, right_height) + 1, True

        h, b = get_height(self.root)
        return b


def test(count, maxkey, debug_print=False):
    bst = BST()
    bst2 = BST()
    keys = []
    for _ in range(count):
        k = random.randint(0, maxkey)
        v = k
        keys.append(k)
        bst.insert_recursive(k, v)
        bst2.insert_non_recursive(k, v)

    # check insert recursive and non recursive get same tree
    if bst != bst2:
        raise Exception('Error insert')

    sorted_keys = sorted(list(set(keys)))
    if debug_print:
        print('sorted keys:')
        print(sorted_keys)

    # inorder
    inorder1 = bst.inorder_traversal_recursive()
    if debug_print:
        print('inorder recursive:')
        print(inorder1)
    if not operator.eq(sorted_keys, inorder1):
        raise Exception('inorder_recursive')

    inorder2 = bst.inorder_traversal_non_recursive()
    if debug_print:
        print('inorder non recursive:')
        print(inorder2)
    if not operator.eq(sorted_keys, inorder2):
        raise Exception('inorder_non_recursive')

    # preorder
    preorder1 = bst.preorder_traversal_recursive()
    if debug_print:
        print('preorder recursive:')
        print(preorder1)

    preorder2 = bst.preorder_traversal_non_recursive()
    if debug_print:
        print('preorder non recursive:')
        print(preorder2)
    if not operator.eq(preorder1, preorder2):
        raise Exception('preorder')

    # postorder
    postorder1 = bst.postorder_traversal_recursive()
    if debug_print:
        print('postorder recursive:')
        print(postorder1)

    postorder2 = bst.postorder_traversal_non_recursive1()
    if debug_print:
        print('postorder non recursive two stack:')
        print(postorder2)
    if not operator.eq(postorder1, postorder2):
        raise Exception('postorder')

    postorder3 = bst.postorder_traversal_non_recursive2()
    if debug_print:
        print('postorder non recursive one stack:')
        print(postorder3)
    if not operator.eq(postorder1, postorder3):
        raise Exception('postorder2')

    if debug_print:
        print('----------------------------------------')


def test_print(count, maxkey):
    bst = BST()
    keys = []
    for _ in range(count):
        k = random.randint(0, maxkey)
        v = k
        keys.append(k)
        bst.insert_recursive(k, v)

    print(keys)
    bst.print_by_level()
    print('---------------------')
    bst.print_zigzag()


def test_balance(count, maxkey):
    bst = BST()
    keys = []
    for _ in range(count):
        k = random.randint(0, maxkey)
        v = k
        keys.append(k)
        bst.insert_recursive(k, v)

    print(bst.is_balance1())
    print(bst.is_balance())
    print('---------------------')


if __name__ == '__main__':
    test_balance(10, 100)
