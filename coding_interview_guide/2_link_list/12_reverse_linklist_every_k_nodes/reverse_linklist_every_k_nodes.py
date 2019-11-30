class Node():
    def __init__(self, val):
        self.val = val
        self.next = None;


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


def reverse_linklist(head):
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre, head


def reverse_linklist_every_k_nodes1(head, k):
    if k < 2 or not head or not head.next:
        return head

    stack = []
    new_head, new_tail = None, None
    cur = head
    while cur:
        next = cur.next
        stack.append(cur)
        if len(stack) == k:
            while len(stack) > 0:
                p = stack.pop()
                if not new_head:
                    new_head = p
                    new_tail = p
                else:
                    new_tail.next = p
                    new_tail = p
            new_tail.next = next
        cur = next

    return new_head



def reverse_linklist_every_k_nodes2(head, k):
    if k < 2 or not head or not head.next:
        return head

    cur = head
    head, tail = None, None
    while cur:
        p = cur
        i = 0
        while i < k-1 and p:
            i += 1
            p = p.next
        
        next = p.next if p else None
        if p:
            p.next = None
            h, t = reverse_linklist(cur)
            if not head:
                head = h
                tail = t
            else:
                tail.next = h
                tail = t
        else:
            tail.next = cur

        cur = next

    return head


def test_reverse_linklist_every_k_nodes(count, k):
    datas = []
    for i in range(count):
        datas.append(i)

    head = make_linklist(datas)
    head = reverse_linklist_every_k_nodes1(head, k)
    l = dump_to_list(head)
    print(l)

    head = make_linklist(datas)
    head = reverse_linklist_every_k_nodes2(head, k)
    l = dump_to_list(head)
    print(l)

    print('--------------------------------------')


if __name__ == '__main__':
    test_reverse_linklist_every_k_nodes(10, 2)
    test_reverse_linklist_every_k_nodes(10, 3)
    test_reverse_linklist_every_k_nodes(10, 4)
    test_reverse_linklist_every_k_nodes(10, 5)
    test_reverse_linklist_every_k_nodes(10, 6)
    test_reverse_linklist_every_k_nodes(10, 7)
    test_reverse_linklist_every_k_nodes(10, 8)
    test_reverse_linklist_every_k_nodes(10, 9)
    test_reverse_linklist_every_k_nodes(10, 10)

