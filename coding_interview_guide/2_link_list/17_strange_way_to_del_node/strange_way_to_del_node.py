class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def make_linklist(count, del_index):
    head, tail = None, None
    node_to_del = None
    for i in range(count):
        node = Node(i)
        if i == del_index:
            node_to_del = node

        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head, node_to_del


def dump_to_list(head):
    l = []
    p = head
    while p:
        l.append(p.val)
        p = p.next

    return l


def del_node(node):
    if not node:
        return

    next = node.next
    if not next:
        raise Exception('Error: can not remove last node')

    node.val = next.val
    node.next = next.next


def test(count, index):
    head, node_to_del = make_linklist(count, index)
    del_node(node_to_del)
    print('remove index:', index)
    print(dump_to_list(head))


if __name__ == '__main__':
    test(10, 0)
    test(10, 1)
    test(10, 5)
    test(10, 8)
    test(10, 10)
    test(10, 9)

