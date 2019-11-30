import random
import operator


class SListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class DListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def remove_countdonw_kth_node_from_slist(head, k):
    if head is None or k < 1:
        return head

    first = head
    while k and first:
        first = first.next
        k -= 1

    if k != 0:
        return head

    if first is None:
        return head.next

    prev = None
    second = head
    while first:
        first = first.next
        prev = second
        second = second.next

    prev.next = second.next
    return head


def remove_countdonw_kth_node_from_slist2(head, k):
    if head is None or k < 1:
        return head

    cur = head
    while cur:
        cur = cur.next
        k -= 1

    if k == 0:
        return head.next

    if k < 0:
        cur = head
        k += 1
        while k != 0:
            cur = cur.next
            k += 1
        cur.next = cur.next.next

    return head


def dump_slist(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next

    return l


def dump_dlist(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next

    return l


def dump_dlist_reverse(head):
    l = []
    if not head:
        return l

    tail = head
    while tail.next:
        tail = tail.next

    while tail:
        l.append(tail.val)
        tail = tail.prev

    return l


def remove_countdonw_kth_node_from_dlist(head, k):
    if head is None or k < 1:
        return head

    first = head
    while k and first:
        first = first.next
        k -= 1

    if k != 0:
        return head

    second = head
    while first:
        first = first.next
        second = second.next

    if second.prev:
        second.prev.next = second.next
    else:
        head.next.prev = None
        return head.next

    if second.next:
        second.next.prev = second.prev

    return head


def make_slist(l):
    head = None
    tail = None
    for a in l:
        node = SListNode(a)
        if tail is None:
            head = node
        else:
            tail.next = node
        tail = node

    return head


def test_single_linklist(count, maxnum, k):
    print(k)
    l = []
    for _ in range(count):
        a = random.randint(0, maxnum)
        l.append(a)


    head1 = make_slist(l)
    head1 = remove_countdonw_kth_node_from_slist(head1, k)

    head2 = make_slist(l)
    head2 = remove_countdonw_kth_node_from_slist2(head2, k)

    l1 = dump_slist(head1)
    l2 = dump_slist(head2)

    print(l)
    if k <= len(l):
        l.pop(len(l) - k)
    print(l1)

    if not operator.eq(l, l1):
        raise Exception('Error1')
    if not operator.eq(l, l2):
        raise Exception('Error2')


def make_dlist(l):
    head = None
    tail = None
    for a in l:
        node = DListNode(a)
        if tail is None:
            head = node
        else:
            tail.next = node
            node.prev = tail
        tail = node

    return head


def test_double_linklist(count, maxnum, k):
    l = []
    for _ in range(count):
        a = random.randint(0, maxnum)
        l.append(a)

    head1 = make_dlist(l)
    head1 = remove_countdonw_kth_node_from_dlist(head1, k)

    print(l)
    if k <= len(l):
        l.pop(len(l) - k)

    l1 = dump_dlist(head1)
    print(l1)
    if not operator.eq(l, l1):
        raise Exception('Error1', l1, l)

    l2 = dump_dlist_reverse(head1)
    if not operator.eq(l, list(reversed(l2))):
        raise Exception('Error2')


if __name__ == '__main__':
    test_single_linklist(10, 20, 1)
    test_single_linklist(10, 20, 8)
    test_single_linklist(10, 20, 16)

    test_single_linklist(100, 200, 10)
    test_single_linklist(100, 200, 80)
    test_single_linklist(100, 200, 160)

    test_double_linklist(10, 20, 1)
    test_double_linklist(10, 20, 8)
    test_double_linklist(10, 20, 10)
    test_double_linklist(10, 20, 16)

    test_double_linklist(100, 200, 10)
    test_double_linklist(100, 200, 80)
    test_double_linklist(100, 200, 160)
