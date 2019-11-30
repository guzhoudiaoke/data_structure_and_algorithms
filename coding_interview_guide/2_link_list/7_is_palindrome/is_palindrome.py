class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList():
    def __init__(self):
        self.head = None


    def init(self, datas):
        tail = None
        for v in datas:
            node = Node(v)
            if tail is None:
                self.head = node
            else:
                tail.next = node
            tail = node


    def to_list(self):
        l = []
        p = self.head
        while p:
            l.append(p.val)
            p = p.next

        return l


    def is_palindrome_stack(self):
        s = []
        cur = self.head
        while cur:
            s.append(cur.val)
            cur = cur.next

        cur = self.head
        while cur:
            if cur.val != s.pop():
                return False
            cur = cur.next

        return True


    def is_palindrome_stack_half(self):
        if self.head is None or self.head.next is None:
            return True

        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        s = []
        cur = slow.next
        while cur:
            s.append(cur.val)
            cur = cur.next

        cur = self.head
        while len(s) > 0:
            if cur.val != s.pop():
                return False
            cur = cur.next

        return True


    def is_palindrome_reverse(self):
        if self.head is None or self.head.next is None:
            return True

        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        half = slow.next
        slow.next = None

        prev = None
        cur = half
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        p1 = self.head
        p2 = prev

        while p1 and p2:
            if p1.val != p2.val:
                return False

            p1 = p1.next
            p2 = p2.next

        return True


def test_palindrome(l):
    ll = LinkList()
    ll.init(l)

    l1 = ll.to_list()
    print(l1)

    print('is_palindrome_stack:     ', ll.is_palindrome_stack())
    print('is_palindrome_stack_half:', ll.is_palindrome_stack_half())
    print('is_palindrome_reverse   :', ll.is_palindrome_reverse())
    print('--------------------')


if __name__ == '__main__':
    test_palindrome([])
    test_palindrome([1])
    test_palindrome([1, 1])
    test_palindrome([1, 2, 1])
    test_palindrome([1, 2, 1, 2])
    test_palindrome([1, 2, 3, 4])
    test_palindrome([1, 2, 3, 4, 3, 2, 1])
    test_palindrome([1, 2, 3, 4, 4, 3, 2, 1])
