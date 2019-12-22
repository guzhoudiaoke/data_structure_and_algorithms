"""
Data Structures And Algorithms:
    check if tree1 contains tree2
"""


class TreeNode():  # pylint: disable=too-few-public-methods
    """
    Binary Tree Node
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def contains(root1, root2):
    """
    check is tree t1 contains t2

    :param root1: the root of tree1
    :param root2: the root of tree2
    """
    def check(root1, root2):
        if root2 is None:
            return True
        if root1 is None or root1.val != root2.val:
            return False

        return (check(root1.left, root2.left) and
                check(root1.right, root2.right))

    if root1 is None:
        return root2 is None

    # root1 contains root2 or
    # root1's left sub tree contains root2 or
    # root1's right sub tree contains root2 or
    return (check(root1, root2) or
            contains(root1.left, root2) or
            contains(root1.right, root2))
