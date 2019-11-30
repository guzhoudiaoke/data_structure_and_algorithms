class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def arrange_linklist_by_half(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head.next
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    left = head
    right = slow.next
    slow.next = None

    head, tail = left, left
    left = left.next
    while left:
        tail.next = right
        tail = right
        right = right.next
        tail.next = left
        tail = left
        left = left.next

    tail.next = right
    return head


def make_linklist(count):
    head, tail = None, None
    for i in range(count):
        node = Node(i)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head


def dump_linklist(head):
    p = head
    l = []
    while p:
        l.append(p.val)
        p = p.next

    return l


def test(count):
    head = make_linklist(count)
    l = dump_linklist(head)
    print(l)

    head = arrange_linklist_by_half(head)
    l = dump_linklist(head)
    print(l)
    print('----------------------------------------------')


if __name__ == '__main__':
    test(0)
    test(1)
    test(2)
    test(3)
    test(4)
    test(10)
    test(11)
    test(12)
    test(13)

