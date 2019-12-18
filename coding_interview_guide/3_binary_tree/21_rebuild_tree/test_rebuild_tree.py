import unittest
import random
import operator
import bst as bst


def make_cbt(count):
    if count == 0:
        return None

    nodes = [bst.TreeNode(i) for i in range(count)]
    for i in range(count):
        left = 2*i + 1
        right = 2*i + 2
        if left < count:
            nodes[i].left = nodes[left]
        if right < count:
            nodes[i].right = nodes[right]

    return nodes[0]


class RebuildTreeTestCase(unittest.TestCase):
    def test_pre_in_rebuild(self):
        test_count = 100
        key_count = 99
        maxkey = 1000
        for __ in range(test_count):
            tree = bst.BST()
            for _ in range(key_count):
                v = random.randint(0, maxkey)
                tree.insert_recursive(v)

            pre_order = tree.preorder_traversal_recursive()
            in_order = tree.inorder_traversal_recursive()
            post_order = tree.postorder_traversal_recursive()

            r = bst.rebuild_tree_by_pre_in_order(pre_order, in_order)
            tree_rebuild = bst.BST(r)
            pre_rebuild = tree_rebuild.preorder_traversal_recursive()
            in_rebuild = tree_rebuild.inorder_traversal_recursive()
            post_rebuild = tree_rebuild.postorder_traversal_recursive()

            self.assertTrue(tree == tree_rebuild)
            self.assertTrue(operator.eq(pre_order, pre_rebuild))
            self.assertTrue(operator.eq(in_order, in_rebuild))
            self.assertTrue(operator.eq(post_order, post_rebuild))

    def test_in_post_rebuild(self):
        test_count = 100
        key_count = 99
        maxkey = 1000
        for __ in range(test_count):
            tree = bst.BST()
            for _ in range(key_count):
                v = random.randint(0, maxkey)
                tree.insert_recursive(v)

            pre_order = tree.preorder_traversal_recursive()
            in_order = tree.inorder_traversal_recursive()
            post_order = tree.postorder_traversal_recursive()

            r = bst.rebuild_tree_by_in_post_order(in_order, post_order)
            tree_rebuild = bst.BST(r)
            pre_rebuild = tree_rebuild.preorder_traversal_recursive()
            in_rebuild = tree_rebuild.inorder_traversal_recursive()
            post_rebuild = tree_rebuild.postorder_traversal_recursive()

            self.assertTrue(tree == tree_rebuild)
            self.assertTrue(operator.eq(pre_order, pre_rebuild))
            self.assertTrue(operator.eq(in_order, in_rebuild))
            self.assertTrue(operator.eq(post_order, post_rebuild))

    def test_pre_post_rebuild(self):
        test_count = 100
        key_count = 99
        for __ in range(test_count):
            tree = bst.BST(make_cbt(key_count))

            pre_order = tree.preorder_traversal_recursive()
            in_order = tree.inorder_traversal_recursive()
            post_order = tree.postorder_traversal_recursive()

            r = bst.rebuild_tree_by_pre_post_order(pre_order, post_order)
            tree_rebuild = bst.BST(r)
            pre_rebuild = tree_rebuild.preorder_traversal_recursive()
            in_rebuild = tree_rebuild.inorder_traversal_recursive()
            post_rebuild = tree_rebuild.postorder_traversal_recursive()

            self.assertTrue(tree == tree_rebuild)
            self.assertTrue(operator.eq(pre_order, pre_rebuild))
            self.assertTrue(operator.eq(in_order, in_rebuild))
            self.assertTrue(operator.eq(post_order, post_rebuild))
