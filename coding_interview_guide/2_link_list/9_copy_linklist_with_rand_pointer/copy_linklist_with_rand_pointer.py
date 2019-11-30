import random
import operator


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None


class LinkList():
    def __init__(self):
        self.head = None
        self.sorted_head = None


    def make_linklist(self, datas):
        if not datas:
            return

        tail = None
        for d in datas:
            node = Node(d)
            if not self.head:
                self.head = node
                self.sorted_head = node
                tail = node
            else:
                tail.next = node
                tail = node

                prev = None
                cur = self.sorted_head
                while cur and cur.val < d:
                    prev = cur
                    cur = cur.rand

                if not prev:
                    node.rand = self.sorted_head
                    self.sorted_head = node
                else:
                    prev.rand = node
                    node.rand = cur


    def to_list(self):
        l = []
        p = self.head
        while p:
            l.append(p.val)
            p = p.next

        return l


    def sorted_to_list(self):
        l = []
        p = self.sorted_head
        while p:
            l.append(p.val)
            p = p.rand

        return l


    def copy(self):
        cp = LinkList()
        if not self.head:
            return cp

        node_map = {}
        p = self.head
        while p:
            node = Node(p.val)
            node_map[p] = node
            p = p.next

        p = self.head
        while p:
            if p.next:
                node_map[p].next = node_map[p.next]
            if p.rand:
                node_map[p].rand = node_map[p.rand]
            p = p.next

        cp.head = node_map[self.head]
        cp.sorted_head = node_map[self.sorted_head]
        return cp


    def copy2(self):
        cp = LinkList()
        if not self.head:
            return cp

        # copy node, and add to list
        p = self.head
        while p:
            node = Node(p.val)
            next = p.next
            p.next = node
            node.next = next
            p = next

        # copy rand
        p = self.head
        while p:
            next = p.next.next
            copy_node = p.next
            if p.rand:
                copy_node.rand = p.rand.next
            p = next

        cp.head = self.head.next
        cp.sorted_head = self.sorted_head.next

        # split from list
        p = self.head
        head = None
        tail = None
        while p:
            next = p.next.next
            copy_node = p.next
            p.next = next
            copy_node.next = None
            if not head:
                head = copy_node
                tail = copy_node
            else:
                tail.next = copy_node
                tail = copy_node
            p = next

        return cp


def test_copy_linklist(count):
    datas = []
    for i in range(count):
        datas.append(i)
    random.shuffle(datas)

    ll = LinkList()
    ll.make_linklist(datas)
    l1 = ll.to_list()
    l2 = ll.sorted_to_list()

    datas_sorted = sorted(datas)
    if not operator.eq(l2, datas_sorted):
        raise Exception('Error')

    cp = ll.copy()
    cp_l1 = cp.to_list()
    if not operator.eq(l1, cp_l1):
        raise Exception('Error')

    cp_l2 = cp.sorted_to_list()
    if not operator.eq(l2, cp_l2):
        raise Exception('Error')

    cp2 = ll.copy2()
    cp2_l1 = cp2.to_list()
    if not operator.eq(l1, cp2_l1):
        raise Exception('Error')

    cp2_l2 = cp2.sorted_to_list()
    if not operator.eq(l2, cp2_l2):
        raise Exception('Error')


if __name__ == '__main__':
    test_copy_linklist(0)
    test_copy_linklist(1)
    test_copy_linklist(10)
    test_copy_linklist(100)
    test_copy_linklist(1000)
    test_copy_linklist(10000)

