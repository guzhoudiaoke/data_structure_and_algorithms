import random
import operator


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_to_sorted_cycle_list(head, val):
    node = Node(val)
    if not head:
        node.next = node
        return node

    pre = head
    cur = head.next
    while cur != head:
        if pre.val <= val and cur.val >= val:
            break

        pre = cur
        cur = cur.next

    pre.next = node
    node.next = cur

    if head.val > val:
        head = node

    return head


def dump_list(head):
    if not head:
        return []

    l = [head.val]
    p = head.next
    while p != head:
        l.append(p.val)
        p = p.next

    return l


def test(count, maxval):
    l = []
    head = None
    for _ in range(count):
        x = random.randint(0, maxval)
        l.append(x)
        head = insert_to_sorted_cycle_list(head, x)

    sorted_l = sorted(l)
    l1 = dump_list(head)
    if not operator.eq(sorted_l, l1):
        raise Exception('Error')


if __name__ == '__main__':
    test(10, 100)
    test(100, 1000)
    test(1000, 10000)
    test(10000, 100000)

