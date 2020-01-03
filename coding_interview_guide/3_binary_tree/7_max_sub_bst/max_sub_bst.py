import sys


class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_sub_bst(root):
    def post_order(node):
        if node is None:
            return None, 0, sys.maxsize, -sys.maxsize

        val, left, right = node.val, node.left, node.right
        l_root, l_num, l_min, l_max = post_order(left)
        r_root, r_num, r_min, r_max = post_order(right)

        if l_root == left and r_root == right and l_max < val < r_min:
            return node, l_num+r_num+1, min(l_min, val), max(r_max, val)

        if l_num > r_num:
            return l_root, l_num, l_min, l_max
        else:
            return r_root, r_num, r_min, r_max

    return post_order(root)


def test_max_sub_bst():
    vals = [6, 1, 12, 0, 3, 10, 13, 4, 14, 20, 16, 2, 5, 11, 15]
    nodes = [TreeNode(v) for v in vals]
    root = nodes[0]
    nodes[0].left, nodes[0].right = nodes[1], nodes[2]
    nodes[1].left, nodes[1].right = nodes[3], nodes[4]
    nodes[2].left, nodes[2].right = nodes[5], nodes[6]
    nodes[5].left, nodes[5].right = nodes[7], nodes[8]
    nodes[6].left, nodes[6].right = nodes[9], nodes[10]
    nodes[7].left, nodes[7].right = nodes[11], nodes[12]
    nodes[8].left, nodes[8].right = nodes[13], nodes[14]

    bst_root, num, min_val, max_val = max_sub_bst(root)
    print(bst_root.val, num, min_val, max_val)


if __name__ == '__main__':
    test_max_sub_bst()
