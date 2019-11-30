class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList():
    def __init__(self):
        self.head = None
        self.cycle_node = None
        self.cycle_length = 0
    

    def make_list(self, length, cycle_length):
        if cycle_length > length:
            return

        non_cycle_length = length - cycle_length
        self.head, tail = None, None
        for i in range(length):
            node = Node(i)
            if not self.head:
                self.head = node
                tail = node
            else:
                tail.next = node
                tail = node

            if i == non_cycle_length:
                self.cycle_node = node

        if self.cycle_node:
            tail.next = self.cycle_node


    def dump(self):
        l = []
        p = self.head
        pass_cycle = False
        while p:
            if p == self.cycle_node:
                pass_cycle = True

            l.append(p.val)
            p = p.next

            if p == self.cycle_node and pass_cycle:
                break

        print(l)
        if self.cycle_node:
            print('cycle at', self.cycle_node.val)
        else:
            print('no cycle')


class IntersectNonCycleLinkLists():
    def __init__(self):
        self.head1 = None
        self.head2 = None
        self.intersect_node = None
        self.common_length = 0


    def make_non_cycle_lists(self, length1, length2, common_length):
        if length1 < 0 or length2 < 0 or common_length < 0:
            return

        if common_length > length1 or common_length > length2:
            return

        self.head1, tail1 = None, None
        for i in range(length1 - common_length):
            node = Node('1_' + str(i))
            if not self.head1:
                self.head1 = node
                tail1 = node
            else:
                tail1.next = node
                tail1 = node

        self.head2, tail2 = None, None
        for i in range(length2 - common_length):
            node = Node('2_' + str(i))
            if not self.head2:
                self.head2 = node
                tail2 = node
            else:
                tail2.next = node
                tail2 = node

        if common_length == 0:
            return

        node = Node('c_0')
        self.intersect_node = node
        self.common_length = common_length

        if tail1:
            tail1.next = node
        else:
            self.head1 = node
        if tail2:
            tail2.next = node
        else:
            self.head2 = node

        tail = node
        for i in range(1, common_length):
            node = Node('c_' + str(i))
            tail.next = node
            tail = node


    def dump(self):
        l = []
        p = self.head1
        while p:
            l.append(p.val)
            p = p.next
        print('l1:', l)

        l = []
        p = self.head2
        while p:
            l.append(p.val)
            p = p.next
        print('l2:', l)

        print('common_length: ', self.common_length)
        print('intersect node: ', self.intersect_node.val if self.intersect_node else 'None')


def have_cycle(head):
    if not head or not head.next:
        return False

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


def get_cycle_node(head):
    if not head or not head.next:
        return None

    cycle = False
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle = True
            break

    print(cycle)
    if not cycle:
        return None

    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return slow


def get_cycle_node2(head):
    if not head or not head.next:
        return None

    move1 = 0
    cycle = False
    slow, fast = head, head
    while fast and fast.next:
        move1 += 1
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle = True
            break

    print(cycle)
    if not cycle:
        return None

    move2 = 0
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
        move2 += 1

    print('slow moves: ', move1, 'meet to entree: ', move2)
    return slow


def get_intersect_node_non_cycle(head1, head2):
    length1 = 0
    p1 = head1
    while p1.next:
        length1 += 1
        p1 = p1.next

    length2 = 0
    p2 = head2
    while p2.next:
        length2 += 1
        p2 = p2.next

    if p1 != p2:
        return None

    p1, p2 = head1, head2
    if length1 > length2:
        delta = length1 - length2
        while delta:
            p1 = p1.next
            delta -= 1
    else:
        delta = length2 - length1
        while delta:
            p2 = p2.next
            delta -= 1

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


def get_intersect_node_cycle(head1, entree1, head2, entree2):
    if entree1 == entree2:
        length1 = 0
        p1 = head1
        while p1 != entree1:
            length1 += 1
            p1 = p1.next

        length2 = 0
        p2 = head2
        while p2 != entree2:
            length2 += 1
            p2 = p2.next

        p1, p2 = head1, head2
        if length1 > length2:
            delta = length1 - length2
            while delta:
                p1 = p1.next
                delta -= 1
        else:
            delta = length2 - length1
            while delta:
                p2 = p2.next
                delta -= 1

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
    else:
        p1 = entree1.next
        while p1 != entree1:
            if p1 == entree2:
                return entree1
            p1 = p1.next

        return None
    

def test_cycle(length, cycle_length):
    print('list length', length, 'cycle length', cycle_length)

    ll = LinkList()
    ll.make_list(length, cycle_length)
    ll.dump()

    print('have cycle:', have_cycle(ll.head)) 
    cycle_node = get_cycle_node(ll.head)
    if cycle_node:
        print('cycle node:', cycle_node.val)
    else:
        print('cycle node:', 'None')

    print('-----------------------------------------')


def test_intersect_non_cycle(length1, length2, common_length):
    print('length1:', length1, 'length2:', length2, 'common_length:', common_length)
    ll = IntersectNonCycleLinkLists()
    ll.make_non_cycle_lists(length1, length2, common_length)
    ll.dump()

    intersect_node = get_intersect_node_non_cycle(ll.head1, ll.head2)
    if intersect_node:
        print('intersect at: ', intersect_node.val)
    else:
        print('intersect at: ', 'None')
    print('-----------------------------------------')


def test_intersect_cycle(length1, length2, common_length, cycle_length):
    print('length1:', length1, 'length2:', length2, 'common_length:', common_length, 'cycle_length', cycle_length)
    ll = IntersectCycleLinkLists()
    ll.make_cycle_lists(length1, length2, common_length, cycle_length)
    ll.dump()

    intersect_node = get_intersect_node_cycle(ll.head1, ll.head2)
    if intersect_node:
        print('intersect at: ', intersect_node.val)
    else:
        print('intersect at: ', 'None')
    print('-----------------------------------------')


if __name__ == '__main__':
    #test_cycle(10, 0)
    #test_cycle(10, 1)
    #test_cycle(10, 2)
    #test_cycle(10, 5)
    #test_cycle(10, 9)
    #test_cycle(10, 10)

    test_intersect_non_cycle(10, 8, 0)
    test_intersect_non_cycle(10, 8, 1)
    test_intersect_non_cycle(10, 8, 2)
    test_intersect_non_cycle(10, 8, 5)
    test_intersect_non_cycle(10, 8, 8)

