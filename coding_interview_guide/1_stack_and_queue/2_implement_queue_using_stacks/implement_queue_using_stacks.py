import random


class Queue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []


    def add(self, data):
        self.push_stack.append(data)


    def poll(self):
        if len(self.pop_stack) == 0 and len(self.push_stack) == 0:
            raise Exception('Queue is empty')

        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())

        return self.pop_stack.pop()


    def peek(self):
        if len(self.pop_stack) == 0 and len(self.push_stack) == 0:
            raise Exception('Queue is empty')

        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())

        return self.pop_stack[-1]


def test(times, maxnum):
    q = Queue()
    q0 = []

    queue_size = 0
    for _ in range(times):
        op = random.randint(0, 1)
        if op == 0 and queue_size > 0:
            a = q.poll()
            b = q0.pop(0)
            print(a, b)
            if a != b:
                raise Exception('Error pop')
            queue_size -= 1
        else:
            r = random.randint(0, maxnum)
            q.add(r)
            q0.append(r)
            if q.peek() != q0[0]:
                raise Exception('Error peek')
            queue_size += 1


if __name__ == '__main__':
    test(1000, 100)

