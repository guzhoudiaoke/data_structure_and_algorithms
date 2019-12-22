"""
unittest for tree1 contains tree2
"""


import unittest
from t1_contains_t2 import contains
from t1_contains_t2 import TreeNode


class T1ContainsT2TestCase(unittest.TestCase):
    """
    unittest for tree1 contains tree2
    """
    def test_same_tree(self):
        """
        test case:
        test tree1 contains tree2 of same tree
        """
        root1 = TreeNode(val=5, left=TreeNode(3), right=TreeNode(7))
        root2 = TreeNode(val=5, left=TreeNode(3), right=TreeNode(7))
        self.assertTrue(contains(root1, root2))

    def test_sub_tree(self):
        """
        test case:
        tree2 is subtree of tree1
        """
        root1 = TreeNode(val=5, left=TreeNode(3), right=TreeNode(7))
        self.assertTrue(contains(root1, root1.left))
        self.assertTrue(contains(root1, root1.right))

    def test_contain(self):
        """
        test case:
        tree1 contains tree2
        """
        root1 = TreeNode(val=5,
                         left=TreeNode(3, left=TreeNode(1), right=TreeNode(4)),
                         right=TreeNode(7, left=TreeNode(6), right=TreeNode(8))
                         )
        root2 = TreeNode(val=7, left=TreeNode(6), right=TreeNode(8))
        root3 = TreeNode(val=7, left=TreeNode(6))
        root4 = TreeNode(val=7, right=TreeNode(8))

        self.assertTrue(contains(root1, root2))
        self.assertTrue(contains(root1, root3))
        self.assertTrue(contains(root1, root4))

    def test_not_contain(self):
        """
        test case:
        tree1 not contains tree2
        """
        root1 = TreeNode(val=5,
                         left=TreeNode(3, left=TreeNode(1), right=TreeNode(4)),
                         right=TreeNode(7, left=TreeNode(6), right=TreeNode(8))
                         )
        root2 = TreeNode(val=7, left=TreeNode(6), right=TreeNode(9))
        root3 = TreeNode(val=9)
        root4 = TreeNode(val=2, right=TreeNode(4))

        self.assertFalse(contains(root1, root2))
        self.assertFalse(contains(root1, root3))
        self.assertFalse(contains(root1, root4))
