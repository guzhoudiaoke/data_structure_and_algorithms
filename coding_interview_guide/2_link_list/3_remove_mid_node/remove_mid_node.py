import math


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
    

def remove_mid_node(head):
    if head is None or head.next is None:
        return head

    if head.next.next is None:
        return head.next;

    pre = head
    cur = head.next.next
    while cur.next is not None and cur.next.next is not None:
        pre = pre.next
        cur = cur.next.next

    pre.next = pre.next.next
    return head


def remove_mid_node2(head):
    if head is None or head.next is None:
        return head

    if head.next.next is None:
        return head.next;

    prev = None
    first = head.next
    second = head
    while first and first.next:
        first = first.next.next
        prev = second
        second = second.next

    prev.next = prev.next.next
    return head


def is_same_list(head1, head2):
    p1 = head1
    p2 = head2
    while p1 and p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next

    return p1 is None and p2 is None


def print_list(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print()


def test_remove_mid_node(count):
    l = []
    for i in range(count):
        l.append(i)

    head1 = None
    tail1 = None
    for a in l:
        node = Node(a)
        if tail1 is None:
            head1 = node
        else:
            tail1.next = node
        tail1 = node

    head2 = None
    tail2 = None
    for a in l:
        node = Node(a)
        if tail2 is None:
            head2 = node
        else:
            tail2.next = node
        tail2 = node

    head1 = remove_mid_node(head1)
    head2 = remove_mid_node2(head2)
    if not is_same_list(head1, head2):
        raise Exception('Error')


def remove_node_by_ratio(head, a, b):
    if a < 1 or a > b:
        return head

    n = 0
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next

    n = math.ceil(n*a / b)
    if n == 1:
        head = head.next

    if n > 1:
        cur = head
        n -= 1
        while n != 1:
            cur = cur.next
            n -= 1
        cur.next = cur.next.next

    return head


def remove_node_by_ratio2(head, a, b):
    if a < 1 or a > b:
        return head

    n = 0
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next

    n = math.ceil(n*a / b)
    if n == 1:
        head = head.next

    prev = None
    cur = head
    for i in range(n-1):
        prev = cur
        cur = cur.next

    if not prev:
        head = head.next
    else:
        prev.next = cur.next
    return head


def test_remove_node_by_ratio(n, a, b):
    l = []
    for i in range(n):
        l.append(i)

    head1 = None
    tail1 = None
    for v in l:
        node = Node(v)
        if tail1 is None:
            head1 = node
        else:
            tail1.next = node
        tail1 = node

    head2 = None
    tail2 = None
    for v in l:
        node = Node(v)
        if tail2 is None:
            head2 = node
        else:
            tail2.next = node
        tail2 = node

    head1 = remove_node_by_ratio(head1, a, b)
    head2 = remove_node_by_ratio2(head2, a, b)
    print_list(head1)
    print_list(head2)


def test_remove_node_by_ratio2(n, a, b):
    l = []
    for i in range(n):
        l.append(i)

    head1 = None
    tail1 = None
    for v in l:
        node = Node(v)
        if tail1 is None:
            head1 = node
        else:
            tail1.next = node
        tail1 = node

    head2 = None
    tail2 = None
    for v in l:
        node = Node(v)
        if tail2 is None:
            head2 = node
        else:
            tail2.next = node
        tail2 = node

    head1 = remove_node_by_ratio(head1, a, b)
    head2 = remove_node_by_ratio2(head2, a, b)

    if not is_same_list(head1, head2):
        raise Exception('Error 2')


if __name__ == '__main__':
    for i in range(100):
        test_remove_mid_node(i)
    
    test_remove_node_by_ratio(7, 1, 6)
    print('-------------------------')
    test_remove_node_by_ratio(7, 3, 6)
    print('-------------------------')
    test_remove_node_by_ratio(7, 5, 6)
    print('-------------------------')
    test_remove_node_by_ratio(7, 6, 6)
    print('-------------------------')
    test_remove_node_by_ratio(7, 1, 4)
    print('-------------------------')
    test_remove_node_by_ratio(7, 2, 4)
    print('-------------------------')
    test_remove_node_by_ratio(7, 3, 4)
    print('-------------------------')

    for n in range(10):
        for i in range(1, n):
            for j in range(1, i):
                test_remove_node_by_ratio2(n, j, i)
            

