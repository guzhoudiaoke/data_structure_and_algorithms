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


def insert_sort(head):
    if not head or not head.next:
        return head

    cur = head.next
    head.next = None
    while cur:
        next = cur.next
        cur.next = None

        prev = None
        p = head
        while p and p.val <= cur.val:
            prev = p
            p = p.next

        if not prev:
            cur.next = head
            head = cur
        else:
            prev.next = cur
            cur.next = p

        cur = next

    return head


def get_smallest_node(head):
    small_pre = None
    small = head

    pre = head
    cur = head.next
    while cur:
        if cur.val < small.val:
            small_pre = pre
            small = cur

        pre = cur
        cur = cur.next

    return small_pre, small


def selection_sort(head):
    if not head or not head.next:
        return head

    tail = None
    cur = head
    while cur:
        small_prev, small = get_smallest_node(cur)
        if small_prev:
            small_prev.next = small.next

        if cur == small:
            cur = cur.next

        small.next = None
        if not tail:
            head = small
            tail = small
        else:
            tail.next = small
            tail = small

    return head


def get_biggest_node(head):
    big_pre = None
    big = head

    pre = head
    cur = head.next
    while cur:
        if cur.val > big.val:
            big_pre = pre
            big = cur

        pre = cur
        cur = cur.next

    return big_pre, big


def selection_sort2(head):
    if not head or not head.next:
        return head

    new_head = None
    while head:
        big_prev, big = get_biggest_node(head)
        if big_prev:
            big_prev.next = big.next

        if head == big:
            head = head.next

        big.next = new_head
        new_head = big

    return new_head


def test(count, maxval):
    datas = []
    for _ in range(count):
        r = random.randint(0, maxval)
        datas.append(r)

    head = make_linklist(datas)
    head = insert_sort(head)
    l = dump_to_list(head)
    if not operator.eq(sorted(datas), l):
        raise Exception('Error')

    head = make_linklist(datas)
    head = selection_sort(head)
    l = dump_to_list(head)
    if not operator.eq(sorted(datas), l):
        raise Exception('Error')

    head = make_linklist(datas)
    head = selection_sort2(head)
    l = dump_to_list(head)
    if not operator.eq(sorted(datas), l):
        raise Exception('Error')


if __name__ == '__main__':
    test(0, 100)
    test(1, 100)
    test(2, 100)
    test(10, 100)
    test(10, 100)
    test(100, 100)
    test(1000, 100)
    test(1000, 10000)

