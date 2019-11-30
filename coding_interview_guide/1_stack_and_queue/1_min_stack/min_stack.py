import random


class MinStack:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []


    def push(self, num):
        self.data_stack.append(num)
        if len(self.min_stack) == 0:
            self.min_stack.append(num)
        else:
            self.min_stack.append(min(num, self.min_stack[-1]))


    def pop(self):
        if len(self.data_stack) == 0:
            raise Exception('Stack is empty')

        self.min_stack.pop()
        return self.data_stack.pop()


    def getmin(self):
        if len(self.data_stack) == 0:
            raise Exception('Stack is empty')

        return self.min_stack[-1]


    def getmin2(self):
        if len(self.data_stack) == 0:
            raise Exception('Stack is empty')

        return min(self.data_stack)


def test_min_stack(times, maxnum):
    s = MinStack()
    stack_size = 0
    for _ in range(times):
        op = random.randint(0, 1)
        if op == 0 and stack_size > 0:
            s.pop()
            stack_size -= 1
        else:
            s.push(random.randint(0, maxnum))
            stack_size += 1

        if stack_size > 0:
            if s.getmin() != s.getmin2():
                raise Exception('Error min')


if __name__ == '__main__':
    test_min_stack(10000, 1000)

