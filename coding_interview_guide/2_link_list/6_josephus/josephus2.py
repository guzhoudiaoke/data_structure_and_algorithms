class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def josephus(head, m):
    if head is None or head.next == head or m < 1:
        return head

    prev, cur = None, head
    x = 0
    while cur != prev:
        x += 1
        if x == m:
            prev.next = cur.next
            x = 0

        next = cur.next
        prev = cur
        cur = cur.next

    return cur.val


def make_cycle_list(l):
    head, tail = None, None
    for x in l:
        node = Node(x)
        if tail is None:
            head = node
        else:
            tail.next = node
        tail = node

    tail.next = head
    return head


def test_josephus(n, m):
    l = []
    for i in range(n):
        l.append(i+1)

    head = make_cycle_list(l)
    x = josephus(head, m)
    print(x)


def get_josephus_live(n, m):
    if n == 1:
        return 0

    return (get_josephus_live(n-1, m) + m) % n


def test_josephus2(n, m):
    x = get_josephus_live(n, m);
    print(x)


if __name__ == '__main__':
    print('6, 5')
    test_josephus(6, 5)
    test_josephus2(6, 5)
    print('------------------------------')

    print('16, 5')
    test_josephus(16, 5)
    test_josephus2(16, 5)
    print('------------------------------')

    print('6, 15')
    test_josephus(6, 15)
    test_josephus2(6, 15)
    print('------------------------------')

    print('500, 123')
    test_josephus(500, 123)
    test_josephus2(500, 123)
    print('------------------------------')

    print('500, 1234')
    test_josephus(500, 1234)
    test_josephus2(500, 1234)
    print('------------------------------')

