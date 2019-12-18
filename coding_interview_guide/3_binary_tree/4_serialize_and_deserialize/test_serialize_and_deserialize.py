import unittest
import random
import bst
import operator


class TestSerializeAndDeserializeCase(unittest.TestCase):
    def test_pre(self):
        for _ in range(100):
            vals = [i for i in range(100)]
            random.shuffle(vals)

            tree = bst.BST()
            for v in vals:
                tree.insert_recursive(v)

            p1 = tree.print_tree()
            s = tree.serialize()
            tree.deserialize(s)
            p2 = tree.print_tree()
            self.assertTrue(operator.eq(p1, p2))

    def test_level(self):
        for _ in range(100):
            vals = [i for i in range(100)]
            random.shuffle(vals)

            tree = bst.BST()
            for v in vals:
                tree.insert_recursive(v)

            p1 = tree.print_tree()
            s = tree.serialize_by_level()
            tree.deserialize_by_level(s)
            p2 = tree.print_tree()
            self.assertTrue(operator.eq(p1, p2))
