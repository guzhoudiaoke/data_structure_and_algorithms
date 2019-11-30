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


    def dump(self):
        print(self.s)


def reverse_print(stack):
    if stack.empty():
        return

    a = stack.pop()
    reverse_print(stack)
    print(a)


def get_and_remove_last2(stack):
    if stack.empty():
        raise Exception('Empty stack')

    a = stack.pop()
    if stack.empty():
        return a

    last = get_and_remove_last(stack)
    stack.push(a)

    return last


def get_and_remove_last(stack):
    if stack.empty():
        raise Exception('Empty stack')

    a = stack.pop()
    if not stack.empty():
        last = get_and_remove_last2(stack)
        stack.push(a)
        return last
    else:
        return a


def reverse(stack):
    if stack.empty():
        return

    a = get_and_remove_last(stack)
    reverse(stack)
    stack.push(a)


def test_stack():
    stack = Stack()
    for i in range(5):
        stack.push(i)

    stack.dump()


def test_reverse_print():
    stack = Stack()
    for i in range(5):
        stack.push(i)

    stack.dump()
    reverse_print(stack)


def test_get_and_remove_last():
    stack = Stack()
    for i in range(5):
        stack.push(i)

    stack.dump()
    for i in range(5):
        last = get_and_remove_last(stack)
        print('last:', last)
        stack.dump()


def test_reverse(times):
    stack = Stack()
    for i in range(times):
        stack.push(i)

    stack.dump()
    reverse(stack)
    stack.dump()


def test_reverse2():
    stack = Stack()
    stack.dump()
    reverse(stack)
    stack.dump()


if __name__ == '__main__':
    #test_stack()
    #print('----------------------')
    #test_reverse_print()
    #print('----------------------')
    #test_get_and_remove_last()
    test_reverse(0)
    test_reverse(1)
    test_reverse(10)
