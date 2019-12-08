import unittest
import random
import operator
import binary_search_tree
import pre_and_in_order_to_post_order as order


def make_random_bst(count, maxkey):
    ret = binary_search_tree.BinarySearchTree()
    keys = []
    for _ in range(count):
        k = random.randint(0, maxkey)
        v = k
        keys.append(k)
        ret.insert_recursive(k, v)
    return ret


class PreOrderInOrderToPostOrderTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple(self):
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        postorder = [4, 5, 2, 6, 7, 3, 1]

        ret = order.pre_order_in_order_to_post_order3(preorder, inorder)
        self.assertTrue(operator.eq(postorder, ret))

    def test_by_make_bst_10_100(self):
        for _ in range(100):
            tree = make_random_bst(10, 100)
            preorder = tree.preorder_traversal_recursive()
            inorder = tree.inorder_traversal_recursive()
            postorder = tree.postorder_traversal_recursive()

            ret1 = order.pre_order_in_order_to_post_order1(preorder, inorder)
            ret2 = order.pre_order_in_order_to_post_order2(preorder, inorder)
            ret3 = order.pre_order_in_order_to_post_order3(preorder, inorder)

            self.assertTrue(operator.eq(postorder, ret1))
            self.assertTrue(operator.eq(postorder, ret2))
            self.assertTrue(operator.eq(postorder, ret3))

    def test_by_make_bst_100_1000(self):
        for _ in range(100):
            tree = make_random_bst(100, 1000)
            preorder = tree.preorder_traversal_recursive()
            inorder = tree.inorder_traversal_recursive()
            postorder = tree.postorder_traversal_recursive()

            ret1 = order.pre_order_in_order_to_post_order1(preorder, inorder)
            ret2 = order.pre_order_in_order_to_post_order2(preorder, inorder)
            ret3 = order.pre_order_in_order_to_post_order3(preorder, inorder)

            self.assertTrue(operator.eq(postorder, ret1))
            self.assertTrue(operator.eq(postorder, ret2))
            self.assertTrue(operator.eq(postorder, ret3))
