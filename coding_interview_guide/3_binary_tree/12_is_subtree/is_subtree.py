"""
Data Structures And Algorithms:
    check if tree2 is subtree of tree1

leetcode 572:
    https://leetcode-cn.com/submissions/detail/40892514/
"""


class TreeNode():  # pylint: disable=too-few-public-methods
    """
    Binary Tree Node
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    """
    serialize tree to string

    :param root: the root of tree
    """
    def preorder(node):
        """
        serialize by pre order traversal

        :param node: the current node to traversal
        """
        if not node:
            return '#|'

        res = '(' + str(node.val) + ')'
        res += preorder(node.left)
        res += preorder(node.right)
        return res

    return preorder(root)


def is_subtree(root1, root2):
    """
    check if tree t2 is subtree of t1

    :param root1: the root of tree1
    :param root2: the root of tree2
    """
    serialize_str1 = serialize(root1)
    serialize_str2 = serialize(root2)
    return serialize_str2 in serialize_str1
