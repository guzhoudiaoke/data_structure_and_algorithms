import unittest
import random
import bst as bst
import operator


class FindSuccessorTestCase(unittest.TestCase):
    def test_find_successor_simple(self):
        count = 10
        data = [i for i in range(count)]
        random.shuffle(data)

        tree = bst.BST()
        for d in data:
            tree.insert_recursive(d)

        inorder = tree.inorder_traversal_recursive()
        node = tree.get_left_node(tree.root)
        successors = []
        while node:
            successors.append(node.val)
            node = tree.successor(node)

        self.assertTrue(operator.eq(inorder, successors))

    def test_find_successor(self):
        test_count = 100
        count = 100

        for _ in range(test_count):
            data = [i for i in range(count)]
            random.shuffle(data)
            tree = bst.BST()
            for d in data:
                tree.insert_recursive(d)

            inorder = tree.inorder_traversal_recursive()
            node = tree.get_left_node(tree.root)
            successors = []
            while node:
                successors.append(node.val)
                node = tree.successor(node)

            self.assertTrue(operator.eq(inorder, successors))
