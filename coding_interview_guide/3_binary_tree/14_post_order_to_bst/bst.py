import random
import operator


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST():
    def __init__(self, root=None):
        self.root = root

    def insert_recursive(self, val):
        def recursive(node, val):
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = recursive(node.left, val)
            elif val > node.val:
                node.right = recursive(node.right, val)
            return node
        self.root = recursive(self.root, val)

    def inorder_traversal_recursive(self):
        def recursive(node):
            if node:
                recursive(node.left)
                result.append(node.val)
                recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def preorder_traversal_recursive(self):
        def recursive(node):
            if node:
                result.append(node.val)
                recursive(node.left)
                recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def postorder_traversal_recursive(self):
        def recursive(node):
            if node:
                recursive(node.left)
                recursive(node.right)
                result.append(node.val)

        result = []
        recursive(self.root)
        return result

    def build_by_post_order(self, post_order):
        def build(start, end):
            if start >= end:
                return None

            v = post_order[end-1]
            root = TreeNode(v)
            index = start
            while index < end and post_order[index] < v:
                index += 1

            root.left = build(start, index)
            root.right = build(index, end-1)
            return root

        self.root = build(0, len(post_order))


def is_post_order(order):
    def check(start, end):
        if start >= end-1:
            return True

        index = start
        while index < end and order[index] < order[end-1]:
            index += 1

        i = index
        while i < end and order[i] > order[end-1]:
            i += 1

        if i != end-1:
            return False

        return check(start, index) and check(index, end-1)

    if not order:
        return False

    return check(0, len(order))


def test(count):
    datas = list(range(count))
    random.shuffle(datas)

    bst = BST()
    for d in datas:
        bst.insert_recursive(d)

    post_order = bst.postorder_traversal_recursive()
    in_order = bst.inorder_traversal_recursive()
    pre_order = bst.preorder_traversal_recursive()

    bst2 = BST()
    bst2.build_by_post_order(post_order)
    post_order2 = bst2.postorder_traversal_recursive()
    in_order2 = bst2.inorder_traversal_recursive()
    pre_order2 = bst2.preorder_traversal_recursive()

    if not operator.eq(pre_order, pre_order2):
        raise Exception('Error')
    if not operator.eq(in_order, in_order2):
        raise Exception('Error')
    if not operator.eq(post_order, post_order2):
        raise Exception('Error')


def test100():
    for i in range(100):
        test(10)
        test(100)
        test(1000)


if __name__ == '__main__':
    test(10)
    test(100)
    test(1000)
    test100()
