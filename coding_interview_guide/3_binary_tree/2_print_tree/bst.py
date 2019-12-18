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

    def print_tree(self):
        def print_inorder(node, height, to, length):
            if not node:
                return

            print_inorder(node.right, height+1, 'v', length)
            val = to + str(node.val) + to
            len_m = len(val)
            len_l = (length - len_m) // 2
            len_r = length - len_m - len_l
            val = ' ' * (len_l) + val + ' ' * (len_r)
            print(' ' * (height*length) + val)
            print_inorder(node.left, height+1, '^', length)

        print('Binary Tree:')
        print_inorder(self.root, 0, 'H', 17)
        print()

    def print_tree2(self):
        def preorder(node):
            if not node:
                print('None', end='')
                return

            print(node.val, end='')
            if node.left or node.right:
                print('(', end='')
                preorder(node.left)
                print(', ', end='')
                preorder(node.right)
                print(')', end='')

        preorder(self.root)
        print()


def test(count):
    vals = [i for i in range(count)]
    random.shuffle(vals)

    bst = BST()
    for v in vals:
        bst.insert_recursive(v)

    bst.print_tree()
    bst.print_tree2()


if __name__ == '__main__':
    test(10)
