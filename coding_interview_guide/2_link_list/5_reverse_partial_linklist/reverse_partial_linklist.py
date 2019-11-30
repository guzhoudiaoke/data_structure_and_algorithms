class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


# reverse [from_idnex, to_index]
def reverse_partial_list(head, from_index, to_index):
    # check head
    if not head:
        return head

    # check from_index
    if from_index < 1 or from_index >= to_index:
        return head

    # find reverse range: (prev, end)
    prev, end = None, None
    cur = head
    index = 0
    while cur:
        index += 1
        if index == from_index-1:
            prev = cur
        if index == to_index+1:
            end = cur
        cur = cur.next

    # check to_index and length
    length = index
    if to_index > length:
        return head

    # reverse
    p = end
    cur = head if not prev else prev.next
    while cur != end:
        next = cur.next
        cur.next = p
        p = cur
        cur = next

    if prev:
        prev.next = p
        return head

    return p


def dump_list(head):
    l = []
    cur = head
    while cur:
        l.append(cur.val)
        cur = cur.next

    return l


def build_list(l):
    head, tail = None, None
    for v in l:
        node = Node(v)
        if not tail:
            head = node
        else:
            tail.next = node
        tail = node

    return head


def test_reverse_list(count, f, t):
    print('reverse from {0} to {1}'.format(f, t))
    l = []
    for i in range(count):
        l.append(i+1)
    print(l)

    head = build_list(l)
    l1 = dump_list(head)
    print(l1)

    head = reverse_partial_list(head, f, t)
    l1 = dump_list(head)
    print(l1)
    print('----------------------------------------')


if __name__ == '__main__':
    test_reverse_list(0, 0, 0)
    test_reverse_list(1, 1, 1)
    test_reverse_list(2, 1, 1)
    test_reverse_list(2, 1, 2)
    test_reverse_list(3, 1, 2)
    test_reverse_list(3, 1, 3)
    test_reverse_list(3, 2, 3)
    test_reverse_list(10, 1, 10)
    test_reverse_list(10, 1, 5)
    test_reverse_list(10, 3, 5)
    test_reverse_list(10, 3, 10)

