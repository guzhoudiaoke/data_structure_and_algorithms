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

            return recursive(lhs.left, rhs.left) and recursive(
                    lhs.right, rhs.right)

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


if __name__ == '__main__':
    test(0, 100)
    test(1, 100)
    test(10, 100, True)
    test(100, 1000)
    test(1000, 10000)
