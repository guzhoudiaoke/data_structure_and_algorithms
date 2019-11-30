import random
import operator


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_sorted_linklist1(head1, head2):
    head, tail = None, None
    while head1 or head2:
        p = None
        if head1 and head2:
            if head1.val < head2.val:
                p = head1
                head1 = head1.next
            else:
                p = head2
                head2 = head2.next
        elif not head1:
            p = head2
            head2 = head2.next
        elif not head2:
            p = head1
            head1 = head1.next

        p.next = None
        if not head:
            head = p
            tail = p
        else:
            tail.next = p
            tail = p

    return head


def merge_sorted_linklist2(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    head, tail = None, None
    while head1 and head2:
        p = None
        if head1.val < head2.val:
            p = head1
            head1 = head1.next
        else:
            p = head2
            head2 = head2.next

        p.next = None
        if not head:
            head = p
            tail = p
        else:
            tail.next = p
            tail = p

    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return head


def merge_sorted_linklist3(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    head = head1 if head1.val < head1.val else head2
    p1 = head1 if head == head1 else head2
    p2 = head2 if head == head1 else head1
    pre, next = None, None

    while p1 and p2:
        if p1.val <= p2.val:
            pre = p1
            p1 = p1.next
        else:
            next = p2.next
            pre.next = p2
            p2.next = p1
            pre = p2
            p2 = next

    pre.next = p2 if p1 is None else p1
    return head


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


def test(count1, count2, maxval):
    l1 = []
    for _ in range(count1):
        x = random.randint(0, maxval)
        l1.append(x)

    l2 = []
    for _ in range(count2):
        x = random.randint(0, maxval)
        l2.append(x)

    l1 = sorted(l1)
    l2 = sorted(l2)
    sorted_l = sorted(l1 + l2)

    head1 = make_linklist(l1)
    head2 = make_linklist(l2)

    head = merge_sorted_linklist1(head1, head2)
    merged_l_1 = dump_to_list(head)

    if not operator.eq(sorted_l, merged_l_1):
        raise Exception('Error')

    head1 = make_linklist(l1)
    head2 = make_linklist(l2)

    head = merge_sorted_linklist2(head1, head2)
    merged_l_2 = dump_to_list(head)

    if not operator.eq(sorted_l, merged_l_2):
        raise Exception('Error')

    head1 = make_linklist(l1)
    head2 = make_linklist(l2)

    head = merge_sorted_linklist3(head1, head2)
    merged_l_3 = dump_to_list(head)

    if not operator.eq(sorted_l, merged_l_3):
        raise Exception('Error')


if __name__ == '__main__':
    test(1, 0, 10)
    test(10, 10, 100)
    test(100, 89, 1000)
    test(1000, 1234, 10000)

