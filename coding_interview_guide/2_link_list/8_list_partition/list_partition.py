import random
import operator


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def make_linklist(datas):
    head = None
    tail = None
    for v in datas:
        node = Node(v)
        if tail is None:
            head = node
        else:
            tail.next = node
        tail = node

    return head


def to_list(head):
    l = []
    p = head
    while p:
        l.append(p.val)
        p = p.next

    return l


def do_partition1(nodes, pivot):
    small = -1
    big = len(nodes)
    index = 0
    while index != big:
        if nodes[index].val < pivot:
            small += 1
            nodes[small], nodes[index] = nodes[index], nodes[small]
            index += 1
        elif nodes[index].val > pivot:
            big -= 1
            nodes[big], nodes[index] = nodes[index], nodes[big]
        else:
            index += 1


def do_partition2(nodes, pivot):
    i = -1
    for j in range(len(nodes)):
        if nodes[j].val <= pivot:
            i += 1
            nodes[i], nodes[j] = nodes[j], nodes[i]
    nodes[i+1] = nodes[len(nodes)-1]


def partition1(head, pivot):
    if not head:
        return head

    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next

    nodes = []
    cur = head
    for i in range(length):
        nodes.append(cur)
        cur = cur.next

    do_partition1(nodes, pivot)
    for i in range(1, length):
        nodes[i-1].next = nodes[i]

    nodes[i].next = None
    return nodes[0]


def partition2(head, pivot):
    if not head:
        return head

    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next

    nodes = []
    cur = head
    for i in range(length):
        nodes.append(cur)
        cur = cur.next

    do_partition2(nodes, pivot)
    for i in range(1, length):
        nodes[i-1].next = nodes[i]

    nodes[i].next = None
    return nodes[0]


def partition3(head, pivot):
    if not head:
        return head

    cur = head
    length = 0
    num_smaller = 0
    num_equal = 0
    while cur:
        if cur.val == pivot:
            num_equal += 1
        elif cur.val < pivot:
            num_smaller += 1
        length += 1
        cur = cur.next

    index_smaller = 0
    index_equal = num_smaller
    index_bigger = num_smaller + num_equal

    nodes = [None for _ in range(length)]
    cur = head
    while cur:
        if cur.val < pivot:
            nodes[index_smaller] = cur
            index_smaller += 1
        elif cur.val == pivot:
            nodes[index_equal] = cur
            index_equal += 1
        else:
            nodes[index_bigger] = cur
            index_bigger += 1
        cur = cur.next

    for i in range(1, length):
        nodes[i-1].next = nodes[i]

    nodes[i].next = None
    return nodes[0]


def partition4(head, pivot):
    if not head:
        return head

    head_smaller, tail_smaller = None, None
    head_equal, tail_equal = None, None
    head_bigger, tail_bigger = None, None

    cur = head
    while cur:
        next = cur.next
        cur.next = None
        if cur.val < pivot:
            if head_smaller is None:
                head_smaller = cur
                tail_smaller = cur
            else:
                tail_smaller.next = cur
                tail_smaller = cur
        elif cur.val == pivot:
            if head_equal is None:
                head_equal = cur
                tail_equal = cur
            else:
                tail_equal.next = cur
                tail_equal = cur
        else:
            if head_bigger is None:
                head_bigger = cur
                tail_bigger = cur
            else:
                tail_bigger.next = cur
                tail_bigger = cur
        cur = next

    head, tail = head_bigger, tail_bigger
    if head_equal:
        tail_equal.next = head
        head = head_equal
    if head_smaller:
        tail_smaller.next = head
        head = head_smaller

    return head


def check_partition(org, l, pivot):
    index = 0
    while index < len(l) and l[index] < pivot:
        index += 1
    while index < len(l) and l[index] == pivot:
        index += 1
    while index < len(l) and l[index] > pivot:
        index += 1

    if index != len(l):
        return False

    org = sorted(org)
    l = sorted(l)
    if not operator.eq(org, l):
        return False
    
    return True


def check_partition4(org, l, pivot):
    smaller = []
    equal = []
    bigger = []
    for x in org:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            bigger.append(x)

    l1 = smaller + equal + bigger
    if not operator.eq(l1, l):
        return False
    
    return True


def test_partition(count, maxval, pivot):
    l = []
    for _ in range(count):
        n = random.randint(0, maxval)
        l.append(n)

    head1 = make_linklist(l)
    head1 = partition1(head1, pivot)
    l1 = to_list(head1)

    if not check_partition(l, l1, pivot):
        raise Exception('Error')

    head2 = make_linklist(l)
    head2 = partition1(head2, pivot)
    l2 = to_list(head2)

    if not check_partition(l, l2, pivot):
        raise Exception('Error')

    head3 = make_linklist(l)
    head3 = partition3(head3, pivot)
    l3 = to_list(head3)

    if not check_partition(l, l3, pivot):
        print(l, l3)
        raise Exception('Error')

    head4 = make_linklist(l)
    head4 = partition4(head4, pivot)
    l4 = to_list(head4)

    if not check_partition4(l, l4, pivot):
        print(l, l4)
        raise Exception('Error')


if __name__ == '__main__':
    test_partition(10, 15, 6)
    test_partition(10, 6, 3)

    test_partition(100, 150, 60)
    test_partition(100, 60, 30)

    test_partition(1000, 1500, 600)
    test_partition(1000, 600, 300)


