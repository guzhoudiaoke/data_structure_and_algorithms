import random


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linklist(head):
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev


def linklist_to_string(head):
    s = ''
    cur = head
    while cur:
        s += str(cur.val)
        cur = cur.next

    return s


def make_rand_list(count1):
    l = []
    for i in range(count1):
        x = random.randint(0, 9)
        if i == 0:
            x = random.randint(1, 9)
        l.append(x)

    return l


def make_linklist(l):
    head, tail = None, None
    for x in l:
        node = Node(x)
        if not tail:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head


def add_linklist1(head1, head2):
    stack1 = []
    stack2 = []

    p = head1
    while p:
        stack1.append(p)
        p = p.next

    p = head2
    while p:
        stack2.append(p)
        p = p.next

    carry = 0
    head = None
    while stack1 and stack2:
        n1 = stack1.pop().val
        n2 = stack2.pop().val
        x = n1 + n2 + carry
        carry = x // 10
        node = Node(x % 10)
        node.next = head
        head = node

    while stack1:
        n1 = stack1.pop()
        x = n1.val + carry
        carry = x // 10
        node = Node(x % 10)
        node.next = head
        head = node

    while stack2:
        n2 = stack2.pop()
        x = n2.val + carry
        carry = x // 10
        node = Node(x % 10)
        node.next = head
        head = node

    if carry:
        x = carry
        node = Node(x % 10)
        node.next = head
        head = node

    return head


def add_linklist2(head1, head2):
    stack1 = []
    stack2 = []

    p = head1
    while p:
        stack1.append(p)
        p = p.next

    p = head2
    while p:
        stack2.append(p)
        p = p.next

    carry = 0
    head = None
    while stack1 or stack2 or carry:
        n1 = stack1.pop().val if stack1 else 0
        n2 = stack2.pop().val if stack2 else 0
        x = n1 + n2 + carry
        carry = x // 10
        node = Node(x % 10)
        node.next = head
        head = node

    return head


def add_linklist3(head1, head2):
    reversed_head1 = reverse_linklist(head1)
    reversed_head2 = reverse_linklist(head2)

    p1, p2 = reversed_head1, reversed_head2
    carry = 0
    head = None
    while p1 or p2 or carry:
        n1 = p1.val if p1 else 0
        n2 = p2.val if p2 else 0
        x = n1 + n2 + carry
        carry = x // 10
        node = Node(x % 10)
        node.next = head
        head = node

        if p1: p1 = p1.next
        if p2: p2 = p2.next

    head1 = reverse_linklist(reversed_head1)
    head2 = reverse_linklist(reversed_head2)
    return head
   

def test_add_linklist(count1, count2):
    datas1 = make_rand_list(count1)
    datas2 = make_rand_list(count2)

    head1 = make_linklist(datas1)
    head2 = make_linklist(datas2)

    s1 = linklist_to_string(head1)
    s2 = linklist_to_string(head2)

    result1 = add_linklist1(head1, head2)
    sresult1 = linklist_to_string(result1)
    if int(s1) + int(s2) != int(sresult1):
        raise Exception('error')

    result2 = add_linklist2(head1, head2)
    sresult2 = linklist_to_string(result2)
    if int(s1) + int(s2) != int(sresult2):
        raise Exception('error')

    result3 = add_linklist3(head1, head2)
    sresult3 = linklist_to_string(result3)
    if int(s1) + int(s2) != int(sresult3):
        raise Exception('error')


if __name__ == '__main__':
    test_add_linklist(5, 5)
    test_add_linklist(5, 6)
    test_add_linklist(6, 5)
    test_add_linklist(150, 150)
    test_add_linklist(149, 150)
    test_add_linklist(150, 151)

