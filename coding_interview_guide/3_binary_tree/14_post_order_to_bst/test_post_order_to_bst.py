import random
import operator
import unittest
from bst import BST
from bst import is_post_order


class PostOrderToBSTTestCase(unittest.TestCase):
    def check_post_order_to_bst_random(self, node_count):
        datas = list(range(node_count))
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

        self.assertTrue(operator.eq(pre_order, pre_order2))
        self.assertTrue(operator.eq(in_order, in_order2))
        self.assertTrue(operator.eq(post_order, post_order2))

    def test_post_order_to_bst_10(self):
        for _ in range(100):
            self.check_post_order_to_bst_random(10)

    def test_post_order_to_bst_100(self):
        for _ in range(100):
            self.check_post_order_to_bst_random(100)

    def test_post_order_to_bst_1000(self):
        for _ in range(100):
            self.check_post_order_to_bst_random(1000)

    def test_is_post_order_10(self):
        for _ in range(100):
            bst = BST()
            datas = list(range(10))
            random.shuffle(datas)
            for d in datas:
                bst.insert_recursive(d)

            post_order = bst.postorder_traversal_recursive()
            self.assertTrue(is_post_order(post_order))

    def test_not_post_order_10(self):
        for _ in range(100):
            bst = BST()
            datas = list(range(10))
            random.shuffle(datas)
            for d in datas:
                bst.insert_recursive(d)

            node = bst.root
            while not node.left or not node.right:
                if not node.left:
                    node = node.right
                if not node.right:
                    node = node.left

            if not node.left or not node.right:
                continue

            node.left, node.right = node.right, node.left
            post_order = bst.postorder_traversal_recursive()
            self.assertFalse(is_post_order(post_order))
