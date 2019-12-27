"""
Data Structures And Algorithms
    find lowest ancestor of tow nodes in a binary tree
"""
import random
from collections import deque


class TreeNode():  # pylint: disable=too-few-public-methods
    """Binary Tree Node
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BST():
    """Binary Search Tree
    """
    def __init__(self):
        self.root = None

    def insert(self, val):
        """insert a val to BST
        """
        def recursive(node, val):
            """recursive insert a val to BST
            """
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = recursive(node.left, val)
            elif val > node.val:
                node.right = recursive(node.right, val)

            return node

        self.root = recursive(self.root, val)

    def search(self, val):
        """search value from BST
        """
        def recursive(node, val):
            """recursive search value from BST
            """
            if node is None:
                return None

            if val < node.val:
                return recursive(node.left, val)
            if val > node.val:
                return recursive(node.right, val)
            return node

        return recursive(self.root, val)


class LowestAncestorRecord1():
    """record of lowest ancestor
    """
    def __init__(self, root):
        self.map = {}
        if root is not None:
            self.map[root] = None

        self.set_map(root)
        # for k, v in self.map.items():
        #     print(k.val, v.val if v else 'None')

    def set_map(self, node):
        """set map for node
        """
        if node is None:
            return
        if node.left is not None:
            self.map[node.left] = node
        if node.right is not None:
            self.map[node.right] = node

        self.set_map(node.left)
        self.set_map(node.right)

    def query(self, node1, node2):
        """query lowest ancestor or node1 and node2
        """
        path = set()
        while node1 in self.map:
            path.add(node1)
            node1 = self.map[node1]

        while node2 not in path:
            node2 = self.map[node2]

        return node2


class LowestAncestorRecord2():
    """record of lowest ancestor, method 2
    """
    def __init__(self, root):
        self.map = {}
        self.set_map(root)
        # for k, v in self.map.items():
        #     print(k[0].val, k[1].val, v.val)

    def set_map(self, node):
        """ set map for node
        """
        if node is None:
            return

        self.process_node(node.left, node)
        self.process_node(node.right, node)
        self.process_left_right(node)

        self.set_map(node.left)
        self.set_map(node.right)

    def process_node(self, node, ancestor):
        """ process node and node's descendant
        map[(node, node's descendant)] = ancestor
        """
        if node is None:
            return

        self.map[(node, ancestor)] = ancestor
        self.process_node(node.left, ancestor)
        self.process_node(node.right, ancestor)

    def process_left_right(self, node):
        """ map[(node of node's left subtree, node of node's right subtree)] = node
        """
        if node is None:
            return

        self.process_left(node.left, node.right, node)
        self.process_left_right(node.left)
        self.process_left_right(node.right)

    def process_left(self, left, right, ancestor):
        """process left
        """
        if left is None:
            return

        self.process_right(left, right, ancestor)
        self.process_left(left.left, right, ancestor)
        self.process_left(left.right, right, ancestor)

    def process_right(self, left, right, ancestor):
        """process right
        """
        if right is None:
            return

        self.map[(left, right)] = ancestor
        self.process_right(left, right.left, ancestor)
        self.process_right(left, right.right, ancestor)

    def query(self, node1, node2):
        """do query
        """
        if node1 == node2:
            return node1

        if (node1, node2) in self.map:
            return self.map[(node1, node2)]
        return self.map[(node2, node1)]


class LowestAncestorRecord3():  # pylint: disable=too-few-public-methods
    """record of lowest ancestor, method 3
    """
    def __init__(self, root):
        self.root = root
        self.map = {}

    def query(self, node1, node2):
        """query lowest ancestor
        """
        if (node1, node2) in self.map:
            return self.map[(node1, node2)]
        if (node2, node1) in self.map:
            return self.map[(node2, node1)]

        ret = lowest_ancestor4(self.root, node1, node2)
        self.map[(node1, node2)] = ret
        return ret


def lowest_ancestor1(root, node1, node2):
    """get lowest ancestor, method 1
    """
    if root is None or root == node1 or root == node2:
        return root

    left = lowest_ancestor1(root.left, node1, node2)
    right = lowest_ancestor1(root.right, node1, node2)
    if left is not None and right is not None:
        return root

    return left if left is not None else right


def lowest_ancestor2(root, node1, node2):
    """
    get lowest ancestor, method 2
    """
    def is_parent_of(parent, child):
        """
        check if parent is parent of child
        """
        if parent is None:
            return False
        if parent == child:
            return True
        return (is_parent_of(parent.left, child) or
                is_parent_of(parent.right, child))

    if root in (None, node1, node2):
        return root

    if is_parent_of(node1, node2):
        return node1
    if is_parent_of(node2, node1):
        return node2

    node = root
    while node:
        if is_parent_of(node.left, node1) and is_parent_of(node.left, node2):
            node = node.left
        elif (is_parent_of(node.right, node1) and
              is_parent_of(node.right, node2)):
            node = node.right
        else:
            return node

    return node


def lowest_ancestor3(root, node1, node2):
    """
    get lowest ancestor, method 3
    """
    def get_path(cur, node, path):
        """
        get path from root to node
        """
        if cur is None:
            return False

        # add current node
        path.append(cur)

        if cur == node:
            return True
        if get_path(cur.left, node, path):
            return True
        if get_path(cur.right, node, path):
            return True

        path.pop()
        return False

    # get path of two nodes
    path1 = []
    path2 = []
    get_path(root, node1, path1)
    get_path(root, node2, path2)

    i = 0
    while i < min(len(path1), len(path2)) and path1[i] == path2[i]:
        i += 1

    return path1[i-1]


def lowest_ancestor4(root, node1, node2):
    """
    get lowest ancestor, method 4
    """
    deq = deque()
    deq.append(root)
    parents_dic = {root: None}
    while node1 not in parents_dic or node2 not in parents_dic:
        node = deq.popleft()
        if node.left is not None:
            parents_dic[node.left] = node
            deq.append(node.left)
        if node.right is not None:
            parents_dic[node.right] = node
            deq.append(node.right)

    ancestors = set()
    while node1:
        ancestors.add(node1)
        node1 = parents_dic[node1]
    while node2 not in ancestors:
        node2 = parents_dic[node2]

    return node2


def test_lowest_ancestor(count, test_count):
    """
    test lowest ancestor
    """
    bst = BST()
    vals = [i for i in range(count)]
    random.shuffle(vals)
    for val in vals:
        bst.insert(val)

    dic = {}
    for i in range(count):
        dic[i] = bst.search(i)

    record1 = LowestAncestorRecord1(bst.root)
    record2 = LowestAncestorRecord2(bst.root)
    record3 = LowestAncestorRecord3(bst.root)

    for __ in range(test_count):
        results = []
        node1 = dic[random.randint(0, count-1)]
        node2 = dic[random.randint(0, count-1)]

        results.append(lowest_ancestor1(bst.root, node1, node2))
        results.append(lowest_ancestor2(bst.root, node1, node2))
        results.append(lowest_ancestor3(bst.root, node1, node2))
        results.append(lowest_ancestor4(bst.root, node1, node2))
        results.append(record1.query(node1, node2))
        results.append(record2.query(node1, node2))
        results.append(record3.query(node1, node2))

        for i in range(1, len(results)):
            if results[i-1].val != results[i].val:
                print(i)
                raise Exception('Error')


if __name__ == '__main__':
    test_lowest_ancestor(10, 1000)
    test_lowest_ancestor(30, 100)
    test_lowest_ancestor(300, 100)
