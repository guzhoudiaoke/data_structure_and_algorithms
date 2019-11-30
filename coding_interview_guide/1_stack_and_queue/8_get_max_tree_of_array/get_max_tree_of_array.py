import random
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, 'cost time:', end - start)
        return result
    return wrapper


class TreeNode():
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

    
    def get_left(self):
        return self._left


    def set_left(self, left):
        self._left = left


    def get_right(self):
        return self._right
        

    def set_right(self, right):
        self._right = right


    def get_value(self):
        return self._value


def pop_stack_and_set_bigger_node(stack, bigger_node_map):
    top = stack.pop()
    if len(stack) == 0:
        bigger_node_map[top] = None
    else:
        bigger_node_map[top] = stack[-1]


def get_max_tree(arr):
    nodes = [ TreeNode(arr[i]) for i in range(len(arr)) ]
    stack = []
    left_first_bigger_node_map = {}
    right_first_bigger_node_map = {}

    for i in range(len(arr)):
        cur = nodes[i]
        while len(stack) and stack[-1].get_value() < cur.get_value():
            pop_stack_and_set_bigger_node(stack, left_first_bigger_node_map)
        stack.append(cur)

    while len(stack):
        pop_stack_and_set_bigger_node(stack, left_first_bigger_node_map)

    #
    for i in range(len(arr)-1, -1, -1):
        cur = nodes[i]
        while len(stack) and stack[-1].get_value() < cur.get_value():
            pop_stack_and_set_bigger_node(stack, right_first_bigger_node_map)
        stack.append(cur)

    while len(stack):
        pop_stack_and_set_bigger_node(stack, right_first_bigger_node_map)
    
    root = None
    for i in range(len(arr)):
        cur = nodes[i]
        left = left_first_bigger_node_map[cur]
        right = right_first_bigger_node_map[cur]

        if left is None and right is None:
            root = nodes[i]
        elif left is None:
            if right.get_left() is None:
                right.set_left(cur)
            else:
                right.set_right(cur)
        elif right is None:
            if left.get_left() is None:
                left.set_left(cur)
            else:
                left.set_right(cur)
        else:
            parent = left if left.get_value() < right.get_value() else right
            if parent.get_left() is None:
                parent.set_left(cur)
            else:
                parent.set_right(cur)
    
    return root


def get_max_tree2(arr):
    nodes = [ TreeNode(arr[i]) for i in range(len(arr)) ]
    stack = []
    left_first_bigger_node_map = {}
    right_first_bigger_node_map = {}

    for i in range(len(arr)):
        cur = nodes[i]
        while len(stack) and stack[-1].get_value() < cur.get_value():
            pop_stack_and_set_bigger_node(stack, left_first_bigger_node_map)
        stack.append(cur)

    while len(stack):
        pop_stack_and_set_bigger_node(stack, left_first_bigger_node_map)

    #
    for i in range(len(arr)-1, -1, -1):
        cur = nodes[i]
        while len(stack) and stack[-1].get_value() < cur.get_value():
            pop_stack_and_set_bigger_node(stack, right_first_bigger_node_map)
        stack.append(cur)

    while len(stack):
        pop_stack_and_set_bigger_node(stack, right_first_bigger_node_map)
    
    root = None
    parent = None
    for i in range(len(arr)):
        cur = nodes[i]
        left = left_first_bigger_node_map[cur]
        right = right_first_bigger_node_map[cur]

        if left is None and right is None:
            root = nodes[i]
        else:
            if left is None:
                parent = right
            elif right is None:
                parent = left
            else:
                parent = left if left.get_value() < right.get_value() else right

            if parent.get_left() is None:
                parent.set_left(cur)
            else:
                parent.set_right(cur)
    
    return root


def get_first_bigger_nodes(nodes, bigger_node_map):
    stack = []
    for i in range(len(nodes)):
        cur = nodes[i]
        while len(stack) and stack[-1].get_value() < cur.get_value():
            pop_stack_and_set_bigger_node(stack, bigger_node_map)
        stack.append(cur)

    while len(stack):
        pop_stack_and_set_bigger_node(stack, bigger_node_map)


def get_max_tree3(arr):
    nodes = [ TreeNode(arr[i]) for i in range(len(arr)) ]
    left_first_bigger_node_map = {}
    right_first_bigger_node_map = {}

    get_first_bigger_nodes(nodes, left_first_bigger_node_map)
    get_first_bigger_nodes(list(reversed(nodes)), right_first_bigger_node_map)
    
    root = None
    for i in range(len(arr)):
        cur = nodes[i]
        left = left_first_bigger_node_map[cur]
        right = right_first_bigger_node_map[cur]

        if left is None and right is None:
            root = nodes[i]
        else:
            parent = None
            if left is None:
                parent = right
            elif right is None:
                parent = left
            else:
                parent = left if left.get_value() < right.get_value() else right

            if parent.get_left() is None:
                parent.set_left(cur)
            else:
                parent.set_right(cur)
    
    return root


def get_max_tree_rec(arr):
    if len(arr) == 0:
        return None

    m = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[m]:
            m = i

    root = TreeNode(arr[m])
    root.set_left(get_max_tree_rec(arr[:m]))
    root.set_right(get_max_tree_rec(arr[m+1:]))

    return root


def get_max_tree_rec2(arr):
    if len(arr) == 0:
        return None

    m = arr.index(max(arr))
    root = TreeNode(arr[m])
    root.set_left(get_max_tree_rec(arr[:m]))
    root.set_right(get_max_tree_rec(arr[m+1:]))

    return root


def get_max_tree4(arr):
    def pop_stack_and_set_bigger_index(stack, bigger_node_map):
        top = stack.pop()
        if len(stack) == 0:
            bigger_node_map[top] = -1
        else:
            bigger_node_map[top] = stack[-1]


    def get_left_first_bigger_index(arr, bigger_node_map):
        stack = []
        for i in range(len(arr)):
            cur = arr[i]
            while len(stack) and arr[stack[-1]] < cur:
                pop_stack_and_set_bigger_index(stack, bigger_node_map)
            stack.append(i)

        while len(stack):
            pop_stack_and_set_bigger_index(stack, bigger_node_map)


    def get_right_first_bigger_index(arr, bigger_node_map):
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            while len(stack) and arr[stack[-1]] < cur:
                pop_stack_and_set_bigger_index(stack, bigger_node_map)
            stack.append(i)

        while len(stack):
            pop_stack_and_set_bigger_index(stack, bigger_node_map)


    nodes = [ TreeNode(arr[i]) for i in range(len(arr)) ]
    left_first_bigger_index_map = {}
    right_first_bigger_index_map = {}

    get_left_first_bigger_index(arr, left_first_bigger_index_map)
    get_right_first_bigger_index(arr, right_first_bigger_index_map)
    
    root = None
    parent_index = -1
    for i in range(len(arr)):
        left = left_first_bigger_index_map[i]
        right = right_first_bigger_index_map[i]
        cur = nodes[i]

        if left == -1 and right == -1:
            root = nodes[i]
        else:
            if left == -1:
                parent_index = right
            elif right == -1:
                parent_index = left
            else:
                parent_index = left if arr[left] < arr[right] else right

            if parent_index > i:
                nodes[parent_index].set_left(cur)
            else:
                nodes[parent_index].set_right(cur)
    
    return root

def get_max_tree5(arr):
    def get_left_first_bigger_index():
        stack = []
        for i in range(len(arr)):
            cur = arr[i]
            while len(stack) and arr[stack[-1]] < cur:
                top = stack.pop()
                if len(stack):
                    left_first_bigger_index_map[top] = stack[-1]
            stack.append(i)

        while len(stack):
            top = stack.pop()
            if len(stack):
                left_first_bigger_index_map[top] = stack[-1]


    def get_right_first_bigger_index():
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            while len(stack) and arr[stack[-1]] < cur:
                top = stack.pop()
                if len(stack):
                    right_first_bigger_index_map[top] = stack[-1]
            stack.append(i)

        while len(stack):
            top = stack.pop()
            if len(stack):
                right_first_bigger_index_map[top] = stack[-1]


    nodes = [ TreeNode(arr[i]) for i in range(len(arr)) ]
    left_first_bigger_index_map = [-1 for _ in range(len(arr))]
    right_first_bigger_index_map = [-1 for _ in range(len(arr))]
    get_left_first_bigger_index()
    get_right_first_bigger_index()
    
    root = None
    parent_index = -1
    for i in range(len(arr)):
        left = left_first_bigger_index_map[i]
        right = right_first_bigger_index_map[i]
        cur = nodes[i]

        if left == -1 and right == -1:
            root = nodes[i]
        else:
            if left == -1:
                parent_index = right
            elif right == -1:
                parent_index = left
            else:
                parent_index = left if arr[left] < arr[right] else right

            if parent_index > i:
                nodes[parent_index].set_left(cur)
            else:
                nodes[parent_index].set_right(cur)
    
    return root


def get_max_tree6(arr):
    def get_left_first_bigger_index():
        stack = []
        result = [-1 for _ in range(len(arr))]
        for i in range(len(arr)):
            while len(stack) and arr[i] > arr[stack[-1]]:
                stack.pop()

            if len(stack):
                result[i] = stack[-1]
            stack.append(i)

        return result


    def get_right_first_bigger_index():
        stack = []
        result = [-1 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            while len(stack) and arr[i] > arr[stack[-1]]:
                stack.pop()

            if len(stack):
                result[i] = stack[-1]
            stack.append(i)

        return result


    nodes = [ TreeNode(arr[i]) for i in range(len(arr)) ]
    left_first_bigger_index_map = get_left_first_bigger_index()
    right_first_bigger_index_map = get_right_first_bigger_index()
    
    root = None
    parent_index = -1
    for i in range(len(arr)):
        left = left_first_bigger_index_map[i]
        right = right_first_bigger_index_map[i]
        cur = nodes[i]

        if left == -1 and right == -1:
            root = nodes[i]
        else:
            if left == -1:
                parent_index = right
            elif right == -1:
                parent_index = left
            else:
                parent_index = left if arr[left] < arr[right] else right

            if parent_index > i:
                nodes[parent_index].set_left(cur)
            else:
                nodes[parent_index].set_right(cur)
    
    return root


def get_max_tree6_1(arr):
    def get_left_first_bigger_index():
        stack = []
        result = [-1 for _ in range(len(arr))]
        for i in range(len(arr)-1, -1, -1):
            while len(stack) and arr[i] > arr[stack[-1]]:
                top = stack.pop()
                result[top] = i
            stack.append(i)

        return result


    def get_right_first_bigger_index():
        stack = []
        result = [-1 for _ in range(len(arr))]
        for i in range(len(arr)):
            while len(stack) and arr[i] > arr[stack[-1]]:
                top = stack.pop()
                result[top] = i
            stack.append(i)

        return result


    nodes = [ TreeNode(arr[i]) for i in range(len(arr)) ]
    left_first_bigger_index_map = get_left_first_bigger_index()
    right_first_bigger_index_map = get_right_first_bigger_index()
    
    root = None
    parent_index = -1
    for i in range(len(arr)):
        left = left_first_bigger_index_map[i]
        right = right_first_bigger_index_map[i]
        cur = nodes[i]

        if left == -1 and right == -1:
            root = nodes[i]
        else:
            if left == -1:
                parent_index = right
            elif right == -1:
                parent_index = left
            else:
                parent_index = left if arr[left] < arr[right] else right

            if parent_index > i:
                nodes[parent_index].set_left(cur)
            else:
                nodes[parent_index].set_right(cur)
    
    return root


def get_max_tree7(arr):
    def get_min_bigger_index():
        stack = []
        result = [-1 for _ in range(len(arr))]
        for i in range(len(arr)):
            while len(stack) and arr[i] > arr[stack[-1]]:
                top = stack.pop()
                if result[top] == -1 or arr[i] < arr[result[top]]:
                    result[top] = i

            if len(stack):
                result[i] = stack[-1]
            stack.append(i)

        return result

    nodes = [ TreeNode(arr[i]) for i in range(len(arr)) ]
    min_bigger_index = get_min_bigger_index()
    
    root = None
    for i in range(len(arr)):
        cur_node = nodes[i]
        index = min_bigger_index[i]
        if index == -1:
            root = cur_node
        else:
            pnode = nodes[index]
            if index > i:
                pnode.set_left(cur_node)
            else:
                pnode.set_right(cur_node)
    
    return root


def traverse_inorder(root, result):
    if root is None:
        return

    traverse_inorder(root.get_left(), result)
    result.append(root.get_value())
    traverse_inorder(root.get_right(), result)


def traverse_preorder(root, result):
    if root is None:
        return

    result.append(root.get_value())
    traverse_preorder(root.get_left(), result)
    traverse_preorder(root.get_right(), result)


@timethis
def test_get_max_tree_rec(arr):
    root = get_max_tree_rec(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree(arr):
    root = get_max_tree(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree2(arr):
    root = get_max_tree2(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree3(arr):
    root = get_max_tree3(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree_rec2(arr):
    root = get_max_tree_rec2(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree4(arr):
    root = get_max_tree4(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree5(arr):
    root = get_max_tree5(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree6(arr):
    root = get_max_tree6(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree7(arr):
    root = get_max_tree7(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


@timethis
def test_get_max_tree6_1(arr):
    root = get_max_tree6_1(arr)
    time_end = time.time()
    result = []
    traverse_preorder(root, result)
    return result


def test1(count):
    arr = []
    for i in range(count):
        arr.append(i)
    random.shuffle(arr)

    test_get_max_tree_rec(arr)
    result1 = test_get_max_tree(arr)
    result2 = test_get_max_tree2(arr)
    result3 = test_get_max_tree3(arr)
    result4 = test_get_max_tree_rec(arr)
    result5 = test_get_max_tree_rec2(arr)
    result6 = test_get_max_tree4(arr)
    result7 = test_get_max_tree5(arr)
    result8 = test_get_max_tree6(arr)
    result9 = test_get_max_tree7(arr)
    result10 = test_get_max_tree6_1(arr)

    for i in range(len(result1)):
        if result1[i] != result2[i]:
            raise Exception('Error 2')
        if result2[i] != result3[i]:
            raise Exception('Error 3')
        if result3[i] != result4[i]:
            raise Exception('Error 4')
        if result4[i] != result5[i]:
            raise Exception('Error 5')
        if result5[i] != result6[i]:
            raise Exception('Error 6')
        if result6[i] != result7[i]:
            raise Exception('Error 7')
        if result7[i] != result8[i]:
            raise Exception('Error 8')
        if result8[i] != result9[i]:
            raise Exception('Error 9')
        if result9[i] != result10[i]:
            raise Exception('Error 10')


def test0():
    arr = [3, 4, 5, 1, 2]
    #arr = [5, 1, 2]
    print(arr)

    root = get_max_tree(arr)
    result = []
    traverse_preorder(root, result)
    print(result)

    root = get_max_tree_rec(arr)
    result = []
    traverse_preorder(root, result)
    print(result)

    root = get_max_tree4(arr)
    result = []
    traverse_inorder(root, result)
    print(result)

    root = get_max_tree5(arr)
    result = []
    traverse_inorder(root, result)
    print(result)

    root = get_max_tree6(arr)
    result = []
    traverse_inorder(root, result)
    print(result)

    root = get_max_tree7(arr)
    result = []
    traverse_inorder(root, result)
    print(result)


if __name__ == '__main__':
    test0()
    print('-----------------------------------')
    test1(1000)
    print('-----------------------------------')
    test1(10000)
    print('-----------------------------------')
    test1(100000)
    print('-----------------------------------')
