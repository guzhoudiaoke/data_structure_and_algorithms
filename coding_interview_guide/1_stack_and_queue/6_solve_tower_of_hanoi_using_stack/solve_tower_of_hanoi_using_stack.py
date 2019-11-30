import sys
from enum import Enum


class Move(Enum):
    LEFT_TO_MID  = 1
    MID_TO_LEFT  = 2
    MID_TO_RIGHT = 3
    RIGHT_TO_MID = 4


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


    def size(self):
        return len(self.s)


def hanoi_rec(n, a, b, c):
    def move(n, f, t):
        steps.append('Move {0} from {1} to {2}'.format(n, f, t))

    def tower_of_hanoi_rec(n, a, b, c):
        if n == 1:
            move(n, a, c)
        else:
            tower_of_hanoi_rec(n-1, a, c, b)
            move(n, a, c)
            tower_of_hanoi_rec(n-1, b, a, c)

    steps = []
    if n == 0:
        return steps

    tower_of_hanoi_rec(n, a, b, c)
    return steps


def hanoi2_rec(n, left, mid, right):
    def move(n, f, t):
        if f == mid or t == mid:
            steps.append('Move {0} from {1} to {2}'.format(n, f, t))
        else:
            steps.append('Move {0} from {1} to {2}'.format(n, f, mid))
            steps.append('Move {0} from {1} to {2}'.format(n, mid, t))

    def tower_of_hanoi2_rec(n, a, b, c):
        if n == 1:
            move(n, a, c)
        elif a == mid or c == mid:
            tower_of_hanoi2_rec(n-1, a, c, b)
            move(n, a, c)
            tower_of_hanoi2_rec(n-1, b, a, c)
        else:
            tower_of_hanoi2_rec(n-1, a, b, c)
            move(n, a, mid)
            tower_of_hanoi2_rec(n-1, c, b, a)
            move(n, mid, c)
            tower_of_hanoi2_rec(n-1, a, b, c)

    steps = []
    if n == 0:
        return steps

    tower_of_hanoi2_rec(n, left, mid, right)
    return steps


def hanoi2_stack(n, left, mid, right):
    def move(act):
        if act == Move.LEFT_TO_MID:
            f, t = left, mid
        elif act == Move.MID_TO_LEFT:
            f, t = mid, left
        elif act == Move.MID_TO_RIGHT:
            f, t = mid, right
        elif act == Move.RIGHT_TO_MID:
            f, t = right, mid
        else:
            raise Exception('Error move')

        f_stack, t_stack = stacks[f], stacks[t]
        if f_stack.top() > t_stack.top():
            raise Exception('Error move')

        steps.append('Move {0} from {1} to {2}'.format(f_stack.top(), f, t))
        actions.append(act)
        t_stack.push(f_stack.pop())


    left_stack = Stack()
    mid_stack = Stack()
    right_stack = Stack()
    stacks = {
        left : left_stack,
        mid  : mid_stack,
        right: right_stack
    }

    left_stack.push(sys.maxsize)
    mid_stack.push(sys.maxsize)
    right_stack.push(sys.maxsize)
    for i in range(n, 0, -1):
        left_stack.push(i)

    steps = []
    actions = []

    move(Move.LEFT_TO_MID)
    while right_stack.size() != n+1:
        prev_act = actions[-1]
        if prev_act == Move.LEFT_TO_MID or prev_act == Move.MID_TO_LEFT:
            # MID_TO_RIGHT or RIGHT_TO_MID
            if stacks[mid].top() < stacks[right].top():
                move(Move.MID_TO_RIGHT)
            else:
                move(Move.RIGHT_TO_MID)
        elif prev_act == Move.MID_TO_RIGHT or prev_act == Move.RIGHT_TO_MID:
            # LEFT_TO_MID or MID_TO_LEFT
            if stacks[mid].top() < stacks[left].top():
                move(Move.MID_TO_LEFT)
            else:
                move(Move.LEFT_TO_MID)
        else:
            raise Exception('Error prev action')

    return steps



def test_hanoi_rec(n):
    steps = hanoi_rec(n, 'A', 'B', 'C')
    for step in steps:
        print(step)
    print('need {0} steps'.format(len(steps)))


def test_hanoi2_rec(n):
    steps = hanoi2_rec(n, 'A', 'B', 'C')
    for step in steps:
        print(step)
    print('need {0} steps'.format(len(steps)))


def test_hanoi2_stack(n):
    steps = hanoi2_stack(n, 'A', 'B', 'C')
    for step in steps:
        print(step)
    print('need {0} steps'.format(len(steps)))


if __name__ == '__main__':
    print('--------------------------------------')
    print('Normal Tower of Hanoi, using recursion:')
    test_hanoi_rec(3)
    print('--------------------------------------')
    print('Changed Tower of Hanoi, using recursion:')
    test_hanoi2_rec(3)
    print('--------------------------------------')
    print('Changed Tower of Hanoi, using stack:')
    test_hanoi2_stack(3)


