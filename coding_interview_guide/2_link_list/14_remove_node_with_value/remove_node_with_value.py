import random
import operator


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def make_linklist(datas):
    head, tail = None, None
    for d in datas:
        node = Node(d)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head


def dump_to_list(head):
    l = []
    p = head
    while p:
        l.append(p.val)
        p = p.next

    return l


def remove_node_with_val1(head, val):
    stack = []
    p = head
    while p:
        if p.val != val:
            stack.append(p)
        p = p.next

    head = None
    while stack:
        p = stack.pop()
        p.next = head
        head = p

    return head



def remove_node_with_val2(head, val):
    while head and head.val == val:
        head = head.next

    if not head:
        return head

    pre = head
    cur = head.next
    while cur:
        if cur.val == val:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next

    return head


def test(count, maxval, val):
    datas = []
    for _ in range(count):
        d = random.randint(0, maxval)
        datas.append(d)

    head = make_linklist(datas)
    l = dump_to_list(head)
    print(l, 'remove', val)

    head = remove_node_with_val1(head, val)
    l = dump_to_list(head)
    print(l)

    head = make_linklist(datas)
    head = remove_node_with_val2(head, val)
    l = dump_to_list(head)
    print(l)

    while val in datas:
        datas.remove(val)
    print(datas)


def test1(count, maxval, val):
    datas = []
    for _ in range(count):
        d = random.randint(0, maxval)
        datas.append(d)

    head = make_linklist(datas)
    head = remove_node_with_val1(head, val)
    l1 = dump_to_list(head)

    head = make_linklist(datas)
    head = remove_node_with_val2(head, val)
    l2 = dump_to_list(head)

    while val in datas:
        datas.remove(val)

    if not operator.eq(datas, l1):
        raise Exception('Error 1')

    if not operator.eq(datas, l2):
        raise Exception('Error 2')


if __name__ == '__main__':
    test(10, 5, 2)
    test(10, 2, 2)
    test(20, 10, 2)
    test(20, 15, 2)
    test1(100, 20, 2)
    test1(200, 20, 2)
    test1(2000, 20, 2)


