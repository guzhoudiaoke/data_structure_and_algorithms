import random
import operator


class BSTNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None


    def insert(self, node):
        y = None
        x = self.root
        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node


    def search(self, key):
        p = self.root
        while p:
            if p.key == key:
                return p
            elif key < p.key:
                p = p.left
            else:
                p = p.right

        return None


    def traversal(self):
        def traversal_rec(node):
            if not node:
                return

            traversal_rec(node.left)
            l.append(node.key)
            traversal_rec(node.right)

        l = []
        traversal_rec(self.root)
        return l


def make_bst(datas):
    bst = BST()
    for d in datas:
        if bst.search(d) == None:
            node = BSTNode(d)
            bst.insert(node)

    return bst


def convert_bst_to_dlinklist1(bst):
    def inorder(node):
        if not node:
            return

        inorder(node.left)
        q.append(node)
        inorder(node.right)


    if not bst.root:
        return None

    q = []
    inorder(bst.root)

    head = q.pop(0)
    head.left = None

    pre = head
    cur = None
    while q:
        cur = q.pop(0)
        pre.right = cur
        cur.left = pre
        pre = cur

    pre.right = None
    return head


def convert_bst_to_dlinklist2(bst):
    def inorder(node):
        if not node:
            return

        inorder(node.left)
        node.left = d['pre']
        if not d['head']:
            d['head'] = node
        else:
            d['pre'].right = node
        d['pre'] = node
        inorder(node.right)


    d = {'head': None, 'pre': None}
    inorder(bst.root)

    return d['head']


def convert_bst_to_dlinklist3(bst):
    def connect(node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1

        tail1, tail2 = node1.left, node2.left
        tail1.right = node2
        node2.left = tail1
        tail2.right = node1
        node1.left = tail2

        return node1


    def convert(node):
        if not node:
            return None

        head_left = convert(node.left)
        head_right = convert(node.right)
        node.left = node
        node.right = node

        return connect(connect(head_left, node), head_right)


    if not bst.root:
        return None

    head = convert(bst.root)
    head.left.right = None
    head.left = None
    return head


def test_bst(count, maxval):
    datas = []
    for _ in range(count):
        d = random.randint(0, maxval)
        datas.append(d)

    bst = make_bst(datas)
    l = bst.traversal()

    datas = sorted(list(set(datas)))
    if not operator.eq(datas, l):
        raise Exception('Error BST')


def dump_dlinklist(head):
    l = []
    p = head
    while p:
        l.append(p.key)
        p = p.right
    
    return l


def dump_dlinklist_reverse(head):
    l = []
    if not head:
        return l

    p = head
    while p.right:
        p = p.right

    while p:
        l.append(p.key)
        p = p.left
    
    return l


def test_convert1(count, maxval):
    datas = []
    for _ in range(count):
        d = random.randint(0, maxval)
        datas.append(d)

    bst = make_bst(datas)
    l = bst.traversal()

    head = convert_bst_to_dlinklist1(bst)
    l1 = dump_dlinklist(head)
    l2 = dump_dlinklist_reverse(head)

    if not operator.eq(l1, l):
        raise Exception('Error convert1')

    l2.reverse()
    if not operator.eq(l1, l2):
        raise Exception('Error convert1')


def test_convert2(count, maxval):
    datas = []
    for _ in range(count):
        d = random.randint(0, maxval)
        datas.append(d)

    bst = make_bst(datas)
    l = bst.traversal()

    head = convert_bst_to_dlinklist2(bst)
    l1 = dump_dlinklist(head)
    l2 = dump_dlinklist_reverse(head)

    if not operator.eq(l1, l):
        raise Exception('Error convert2')

    l2.reverse()
    if not operator.eq(l1, l2):
        raise Exception('Error convert2')


def test_convert3(count, maxval):
    datas = []
    for _ in range(count):
        d = random.randint(0, maxval)
        datas.append(d)

    bst = make_bst(datas)
    l = bst.traversal()

    head = convert_bst_to_dlinklist3(bst)
    l1 = dump_dlinklist(head)
    l2 = dump_dlinklist_reverse(head)

    if not operator.eq(l1, l):
        raise Exception('Error convert2')

    l2.reverse()
    if not operator.eq(l1, l2):
        raise Exception('Error convert2')


if __name__ == '__main__':
    test_bst(0, 1)
    test_bst(1, 1)
    test_bst(10, 10)
    test_bst(100, 100)
    test_bst(1000, 1000)
    test_bst(10000, 10000)

    test_convert1(0, 1)
    test_convert1(1, 1)
    test_convert1(10, 10)
    test_convert1(100, 100)
    test_convert1(1000, 1000)
    test_convert1(10000, 10000)

    test_convert2(0, 1)
    test_convert2(1, 1)
    test_convert2(10, 10)
    test_convert2(100, 100)
    test_convert2(1000, 1000)
    test_convert2(10000, 10000)

    test_convert3(0, 1)
    test_convert3(1, 1)
    test_convert3(10, 10)
    test_convert3(100, 100)
    test_convert3(1000, 1000)
    test_convert3(10000, 10000)

