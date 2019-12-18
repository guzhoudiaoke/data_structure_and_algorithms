import random


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BST():
    def __init__(self, root=None):
        self.root = root

    def insert_recursive(self, val):
        def recursive(node, val):
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = recursive(node.left, val)
                node.left.parent = node
            elif val > node.val:
                node.right = recursive(node.right, val)
                node.right.parent = node

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

    # leetcode 543
    def max_distance(self):
        def post_order(node):
            if node is None:
                record[0] = 0
                return 0

            lmax = post_order(node.left)
            max_from_left = record[0]

            rmax = post_order(node.right)
            max_from_right = record[0]

            cur_max = max_from_left + max_from_right + 1
            record[0] = max(max_from_left, max_from_right) + 1

            return max(max(lmax, rmax), cur_max)

        if not self.root:
            return 0

        record = [0]
        return post_order(self.root) - 1

    def max_distance2(self):
        def depth(node):
            if not node:
                return 0

            ldepth = depth(node.left)
            rdepth = depth(node.right)
            result[0] = max(result[0], ldepth+rdepth+1)

            return max(ldepth, rdepth)+1

        result = [0]
        depth(self.root)
        return result[0] - 1

    def max_distance3(self):
        def depth(node):
            nonlocal result
            if not node:
                return 0

            ldepth = depth(node.left)
            rdepth = depth(node.right)
            result = max(result, ldepth+rdepth+1)

            return max(ldepth, rdepth)+1

        result = 0
        depth(self.root)
        return result - 1


def test(count):
    vals = [i for i in range(count)]
    random.shuffle(vals)

    bst = BST()
    for v in vals:
        bst.insert_recursive(v)

    print(bst.max_distance())
    print(bst.max_distance2())
    print(bst.max_distance3())


if __name__ == '__main__':
    test(10)
    test(100)
    test(1000)
