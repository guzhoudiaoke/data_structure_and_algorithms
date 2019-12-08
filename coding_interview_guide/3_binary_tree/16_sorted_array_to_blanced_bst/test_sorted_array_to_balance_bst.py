import unittest
import operator
import random
import bst as bst


class SortedArrayToBalanceBSTTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tree = bst.BinarySearchTree()
        tree.generate_by_sorted_array(arr)

        inorder = tree.inorder_traversal_recursive()
        self.assertTrue(operator.eq(arr, inorder))
        self.assertTrue(tree.is_bst())
        self.assertTrue(tree.is_balance())

    def test_random(self):
        test_count = 10
        count = 100
        maxval = 1000

        for _ in range(test_count):
            arr = []
            for i in range(count):
                d = random.randint(0, maxval)
                arr.append(d)

            arr = sorted(list(set(arr)))

            arr = sorted(arr)
            tree = bst.BinarySearchTree()
            tree.generate_by_sorted_array(arr)

            inorder = tree.inorder_traversal_recursive()
            self.assertTrue(operator.eq(arr, inorder))
            self.assertTrue(tree.is_bst())
            self.assertTrue(tree.is_balance())
