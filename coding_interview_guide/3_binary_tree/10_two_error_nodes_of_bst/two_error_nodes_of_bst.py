import random
import operator


class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, val):
        def recursive(node, val):
            if node is None:
                return TreeNode(val)

            if val < node.val:
                node.left = recursive(node.left, val)
            elif val > node.val:
                node.right = recursive(node.right, val)
            return node

        self.root = recursive(self.root, val)

    def inorder_traversal(self):
        def recursive(node):
            if node is None:
                return

            recursive(node.left)
            result.append(node.val)
            recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def search(self, val):
        def recursive(node, val):
            if node is None:
                return None

            if val < node.val:
                return recursive(node.left, val)
            if val > node.val:
                return recursive(node.right, val)
            return node

        return recursive(self.root, val)


def get_two_error_nodes_of_bst(root):
    error_nodes = [None, None]
    if root is None:
        return error_nodes

    stack = []
    prev = None
    node = root
    while stack or node:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if prev is not None and prev.val > node.val:
                if error_nodes[0] is None:
                    error_nodes[0] = prev
                error_nodes[1] = node
            prev = node
            node = node.right

    return error_nodes


def get_parents(root, error_node1, error_node2):
    parents = [None, None]
    if root is None:
        return parents

    stack = []
    node = root
    while stack or node:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.left == error_node1 or node.right == error_node1:
                parents[0] = node
            if node.left == error_node2 or node.right == error_node2:
                parents[1] = node
            node = node.right
    return parents


def fix_bst_with_two_error_nodes1(root):
    e1, e2 = get_two_error_nodes_of_bst(root)
    p1, p2 = get_parents(root, e1, e2)
    l1, r1 = e1.left, e1.right
    l2, r2 = e2.left, e2.right

    if e1 == root:
        if e1 == p2:
            # case 1
            e1.left, e1.right = l2, r2
            e2.left, e2.right = l1, e1
        elif p2.left == e2:
            # case 2
            p2.left = e1
            e2.left, e2.right = l1, r1
            e1.left, e1.right = l2, r2
        else:
            # case 3
            p2.right = e1
            e2.left, e2.right = l1, r1
            e1.left, e1.right = l2, r2
        root = e2
    elif e2 == root:
        if e2 == p1:
            # case 4
            e2.left, e2.right = l1, r1
            e1.left, e1.right = e2, r2
        elif p1.left == e1:
            # case 5
            p1.left = e2
            e1.left, e1.right = l2, r2
            e2.left, e2.right = l1, r1
        else:
            # case 6
            p1.right = e2
            e1.left, e1.right = l2, r2
            e2.left, e2.right = l1, r1
        root = e1
    else:
        if e1 == p2:
            if p1.left == e1:
                # case 7
                p1.left = e2
                e1.left, e1.right = l2, r2
                e2.left, e2.right = l1, e1
            else:
                # case 8
                p1.right = e2
                e1.left, e1.right = l2, r2
                e2.left, e2.right = l1, e1
        elif e2 == p1:
            if p2.left == e2:
                # case 9
                p2.left = e1
                e2.left, e2.right = l1, r1
                e1.left, e1.right = e2, r2
            else:
                # case 10
                p2.right = e1
                e2.left, e2.right = l1, r1
                e1.left, e1.right = e2, r2
        else:
            if p1.left == e1:
                if p2.left == e2:
                    # case 11
                    e1.left, e1.right = l2, r2
                    e2.left, e2.right = l1, r1
                    p1.left = e2
                    p2.left = e1
                else:
                    # case 12
                    e1.left, e1.right = l2, r2
                    e2.left, e2.right = l1, r1
                    p1.left = e2
                    p2.right = e1
            else:
                if p2.left == e2:
                    # case 13
                    e1.left, e1.right = l2, r2
                    e2.left, e2.right = l1, r1
                    p1.right = e2
                    p2.left = e1
                else:
                    # case 14
                    e1.left, e1.right = l2, r2
                    e2.left, e2.right = l1, r1
                    p1.right = e2
                    p2.right = e1

    return root


def fix_bst_with_two_error_nodes2(root):
    e1, e2 = get_two_error_nodes_of_bst(root)
    p1, p2 = get_parents(root, e1, e2)
    l1, r1 = e1.left, e1.right
    l2, r2 = e2.left, e2.right

    if e1 == root:
        if e1 == p2:
            # case 1
            e2.left, e2.right = l1, e1
            e1.left, e1.right = l2, r2
        elif p2.left == e2:
            # case 2
            p2.left = e1
            e2.left, e2.right = l1, r1
            e1.left, e1.right = l2, r2
        else:
            # case 3
            p2.right = e1
            e2.left, e2.right = l1, r1
            e1.left, e1.right = l2, r2

        root = e2
    elif e2 == root:
        if e2 == p1:
            # case 4
            e1.left, e1.right = e2, r2
            e2.left, e2.right = l1, r1
        elif p1.left == e1:
            # case 5
            p1.left = e2
            e1.left, e1.right = l2, r2
            e2.left, e2.right = l1, r1
        else:
            # case 6
            p1.right = e2
            e1.left, e1.right = l2, r2
            e2.left, e2.right = l1, r1

        root = e1
    else:
        if e1 == p2:
            if p1.left == e1:
                # case 7
                p1.left = e2
            else:
                # case 8
                p1.right = e2

            e1.left, e1.right = l2, r2
            e2.left, e2.right = l1, e1
        elif e2 == p1:
            if p2.left == e2:
                # case 9
                p2.left = e1
            else:
                # case 10
                p2.right = e1

            e2.left, e2.right = l1, r1
            e1.left, e1.right = e2, r2
        else:
            if p1.left == e1:
                if p2.left == e2:
                    # case 11
                    p1.left = e2
                    p2.left = e1
                else:
                    # case 12
                    p1.left = e2
                    p2.right = e1
            else:
                if p2.left == e2:
                    # case 13
                    p1.right = e2
                    p2.left = e1
                else:
                    # case 14
                    p1.right = e2
                    p2.right = e1

            e1.left, e1.right = l2, r2
            e2.left, e2.right = l1, r1

    return root


def test_get_two_error_nodes_of_bst(count):
    test = 0
    while test < 10:
        vals = [i for i in range(count)]
        random.shuffle(vals)
        bst = BinarySearchTree()
        for v in vals:
            bst.insert(v)

        node1 = bst.search(random.randint(0, count-1))
        node2 = bst.search(random.randint(0, count-1))
        if node1 != node2:
            inorder1 = bst.inorder_traversal()
            node1.val, node2.val = node2.val, node1.val
            err1, err2 = get_two_error_nodes_of_bst(bst.root)

            if node1.val < node2.val:
                node2, node1 = node1, node2

            if node1 != err1 or node2 != err2:
                raise Exception('Error')

            node1.val, node2.val = node2.val, node1.val
            inorder2 = bst.inorder_traversal()

            if not operator.eq(inorder1, inorder2):
                raise Exception('Error')

            test += 1
    print('test_get_two_error_nodes_of_bst pass')


def test_fix_bst_with_two_error_nodes1(count):
    test = 0
    while test < 10:
        vals = [i for i in range(count)]
        random.shuffle(vals)
        bst = BinarySearchTree()
        for v in vals:
            bst.insert(v)

        node1 = bst.search(random.randint(0, count-1))
        node2 = bst.search(random.randint(0, count-1))
        if node1 != node2:
            inorder1 = bst.inorder_traversal()

            node1.val, node2.val = node2.val, node1.val
            inorder2 = bst.inorder_traversal()

            bst.root = fix_bst_with_two_error_nodes1(bst.root)
            inorder3 = bst.inorder_traversal()

            if not operator.eq(inorder1, inorder3):
                print('org:', inorder1)
                print('err:', inorder2)
                print('fix:', inorder3)
                raise Exception('Error')

            test += 1
    print('test_fix_bst_with_two_error_nodes1 pass')


def test_fix_bst_with_two_error_nodes2(count):
    test = 0
    while test < 10:
        vals = [i for i in range(count)]
        random.shuffle(vals)
        bst = BinarySearchTree()
        for v in vals:
            bst.insert(v)

        node1 = bst.search(random.randint(0, count-1))
        node2 = bst.search(random.randint(0, count-1))
        if node1 != node2:
            inorder1 = bst.inorder_traversal()

            node1.val, node2.val = node2.val, node1.val
            inorder2 = bst.inorder_traversal()

            bst.root = fix_bst_with_two_error_nodes2(bst.root)
            inorder3 = bst.inorder_traversal()

            if not operator.eq(inorder1, inorder3):
                print('org:', inorder1)
                print('err:', inorder2)
                print('fix:', inorder3)
                raise Exception('Error')

            test += 1
    print('test_fix_bst_with_two_error_nodes2 pass')


if __name__ == '__main__':
    test_get_two_error_nodes_of_bst(10)
    test_get_two_error_nodes_of_bst(100)
    test_get_two_error_nodes_of_bst(1000)

    test_fix_bst_with_two_error_nodes1(10)
    test_fix_bst_with_two_error_nodes1(100)
    test_fix_bst_with_two_error_nodes1(1000)

    test_fix_bst_with_two_error_nodes2(10)
