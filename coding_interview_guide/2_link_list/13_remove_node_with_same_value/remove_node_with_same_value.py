import random


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


def remove_node_with_same_val1(head):
    if not head:
        return head

    d = {head.val : True}
    pre = head
    cur = head.next
    while cur:
        if cur.val in d:
            pre.next = cur.next
        else:
            d[cur.val] = True
            pre = cur

        cur = cur.next

    return head


def find_val_in_linklist(head, val):
    p = head
    while p:
        if p.val == val:
            return True
        p = p.next

    return False


def remove_node_with_same_val2(head):
    if not head:
        return head

    cur = head.next
    head.next = None
    tail = head
    while cur:
        next = cur.next
        cur.next = None
        if not find_val_in_linklist(head, cur.val):
            tail.next = cur
            tail = cur
        cur = next

    return head


def test(count, maxval):
    datas = []
    for _ in range(count):
        d = random.randint(0, maxval)
        datas.append(d)

    head = make_linklist(datas)
    l = dump_to_list(head)
    print(l)

    head = remove_node_with_same_val1(head)
    l = dump_to_list(head)
    print(l)

    head = make_linklist(datas)
    head = remove_node_with_same_val2(head)
    l = dump_to_list(head)
    print(l)

    print('---------------------------------')


if __name__ == '__main__':
    test(10, 1)
    test(10, 2)
    test(10, 5)
    test(10, 6)
    test(10, 7)


