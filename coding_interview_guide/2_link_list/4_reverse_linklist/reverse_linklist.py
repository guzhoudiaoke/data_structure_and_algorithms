class SListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class DListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def reverse_slist(head):
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev


def dump_slist(head):
    l = []
    cur = head
    while cur:
        l.append(cur.val)
        cur = cur.next

    return l


def dump_dlist(head):
    l = []
    cur = head
    while cur:
        l.append(cur.val)
        cur = cur.next

    return l


def dump_dlist_reverse(head):
    tail = head
    while tail and tail.next:
        tail = tail.next

    l = []
    cur = tail
    while cur:
        l.append(cur.val)
        cur = cur.prev

    return l


def reverse_dlist(head):
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        if prev:
            prev.prev = cur
        prev = cur
        cur = next

    if prev:
        prev.prev = None
    return prev


def reverse_dlist2(head):
    pre, cur = None, head
    while cur:
        next = cur.next
        cur.next = pre
        cur.prev = next
        pre = cur
        cur = next
    return pre


def test_reverse_slist(count):
    l = []
    for i in range(count):
        l.append(i)

    head, tail = None, None
    for v in l:
        node = SListNode(v)
        if not tail:
            head = node
        else:
            tail.next = node
        tail = node

    print('org data:', l)

    l1 = dump_slist(head)
    print('slist:   ', l1)

    head = reverse_slist(head)
    l1 = dump_slist(head)
    print('reversed:', l1)
    print('-------------------------------------------------')


def test_reverse_dlist(count):
    l = []
    for i in range(count):
        l.append(i)

    head, tail = None, None
    for v in l:
        node = DListNode(v)
        if not tail:
            head = node
        else:
            tail.next = node
            node.prev = tail
        tail = node

    l1 = dump_dlist(head)
    print('dlist:          ', l1)

    l1 = dump_dlist_reverse(head)
    print('reverse print:  ', l1)

    head = reverse_dlist(head)
    l1 = dump_dlist(head)
    print('reversed dlist: ', l1)
    l1 = dump_dlist_reverse(head)
    print('reverse print:  ', l1)

    head = reverse_dlist2(head)
    l1 = dump_dlist(head)
    print('reversed dlist2:', l1)
    l1 = dump_dlist_reverse(head)
    print('reverse print:  ', l1)
    print('-------------------------------------------------')



if __name__ == '__main__':
    test_reverse_slist(0)
    test_reverse_slist(1)
    test_reverse_slist(2)
    test_reverse_slist(3)
    test_reverse_slist(10)

    test_reverse_dlist(0)
    test_reverse_dlist(1)
    test_reverse_dlist(2)
    test_reverse_dlist(3)
    test_reverse_dlist(10)


