import random


class Stack:
    def __init__(self):
        self.s = []


    def push(self, data):
        self.s.append(data)


    def pop(self):
        return self.s.pop()


    def empty(self):
        return len(self.s) == 0


    def top(self):
        return self.s[-1]


def sort_stack(s):
    helper = Stack()
    while not s.empty():
        a = s.pop()
        while not helper.empty() and helper.top() > a:
            s.push(helper.pop())
        helper.push(a)

    while not helper.empty():
        s.push(helper.pop())


def test_sort_stack(times, maxnum):
    s = Stack()
    l = []
    for _ in range(times):
        a = random.randint(0, maxnum)
        s.push(a)
        l.append(a)

    sort_stack(s)
    l.sort()
    while not s.empty():
        a = s.pop()
        b = l.pop(0)
        if a != b:
            raise Exception('Error')


if __name__ == '__main__':
    test_sort_stack(1000, 10000)
