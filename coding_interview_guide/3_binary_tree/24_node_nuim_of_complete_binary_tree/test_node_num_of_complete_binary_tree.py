import unittest
import node_num_of_complete_binary_tree as cbt
import random


class NodeNumOfCompleteBinaryTreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_cbt(self, count):
        if count == 0:
            return None

        nodes = [cbt.TreeNode(i) for i in range(count)]
        for i in range(count):
            left = 2*i + 1
            right = 2*i + 2
            if left < count:
                nodes[i].left = nodes[left]
            if right < count:
                nodes[i].right = nodes[right]

        return nodes[0]

    def test_sequence(self):
        for i in range(10):
            root = self.make_cbt(i)
            cnt = cbt.node_num_of_cbt(root)
            self.assertTrue(cnt == i)

    def test_random(self):
        for i in range(10):
            count = random.randint(0, 100)
            root = self.make_cbt(count)
            cnt = cbt.node_num_of_cbt(root)
            self.assertTrue(cnt == count)
