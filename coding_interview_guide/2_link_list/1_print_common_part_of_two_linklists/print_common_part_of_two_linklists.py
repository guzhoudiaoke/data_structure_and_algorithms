import random
import operator


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(head):
    while head:
        print(head.value, end='->')
        head = head.next
    print()


def print_common_part(head1, head2):
    ans = []
    while head1 and head2:
        if head1.value < head2.value:
            head1 = head1.next
        elif head2.value < head1.value:
            head2 = head2.next
        else:
            ans.append(head1.value)
            head1 = head1.next
            head2 = head2.next

    return ans


def test(count, maxnum):
    head1, head2 = None, None
    tail1, tail2 = None, None

    l1 = []
    for i in range(maxnum):
        l1.append(i)

    l2 = []
    for i in range(maxnum):
        l2.append(i)

    random.shuffle(l1)
    l1 = l1[:count+1]
    l1.sort()

    random.shuffle(l2)
    l2 = l2[:count+1]
    l2.sort()

    for a in l1:
        node = Node(a)
        if head1 is None:
            head1 = node
        else:
            tail1.next = node
        tail1 = node

    for a in l2:
        node = Node(a)
        if head2 is None:
            head2 = node
        else:
            tail2.next = node
        tail2 = node

    common = print_common_part(head1, head2)

    s = set(l1) & set(l2)
    l = list(s)
    l.sort()

    if not operator.eq(l, common):
        raise Exception('Error common')


if __name__ == '__main__':
    test(10, 20)
    test(100, 200)
    test(1000, 2000)
    test(10000, 20000)

