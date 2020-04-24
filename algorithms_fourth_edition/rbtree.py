import random


class TreeNode():
    RED = True
    BLACK = False

    def __init__(self, key, val, color, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.color = color


class RBTree():
    def __init__(self):
        self._root = None

    def contains(self, key):
        return self.get(key) is not None

    def is_empty(self):
        return self._root is None

    def min(self):
        if self.is_empty():
            raise Exception('calls min with empty RBTree')
        return self._min(self._root)

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def is_red(self, node):
        if node is None:
            return False
        return node.color == TreeNode.RED

    def get(self, key):
        if key is None:
            raise Exception('calls get() with key is None')
        return self._get(self._root, key)

    def _get(self, node, key):
        if node is None:
            return None

        if key < node.key:
            return self._get(node.left, key)
        if key > node.key:
            return self._get(node.right, key)
        return node.val

    def put(self, key, val):
        if key is None:
            raise Exception('calls put() with key is None')
        self._root = self._put(self._root, key, val)
        self.check()

    def _put(self, node, key, val):
        if node is None:
            return TreeNode(key, val, TreeNode.RED)

        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = TreeNode.RED
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = TreeNode.RED
        return x

    def flip_colors(self, h):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def delete(self, key):
        if key is None:
            raise Exception('when call delete() key is None')
        if not self.contains(key):
            return

        if not self.is_red(self._root.left) and not self.is_red(self._root.right):
            self._root.color = TreeNode.RED

        self._root = self._delete(self._root, key)
        if not self.is_empty():
            self._root.color = TreeNode.BLACK

        self.check()

    def _delete(self, h, key):
        if key < h.key:
            if not self.is_red(h.left) and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            if key == h.key and h.right is None:
                return None
            if not self.is_red(h.right) and not self.is_red(h.right.left):
                h = self.move_red_right(h)
            if key == h.key:
                x = self._min(h.right)
                h.key = x.key
                h.val = x.val
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)
        return self.balance(h)

    def move_red_left(self, h):
        self.flip_colors(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h

    def move_red_right(self, h):
        self.flip_colors(h)
        if self.is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h

    def delete_min(self):
        if self.is_empty():
            raise Exception('BST underflow')
        if not self.is_red(self._root.left) and not self.is_red(self._root.right):
            self._root.color = TreeNode.RED

        self._root = self._delete_min(self._root)
        if not self.is_empty():
            self._root.color = TreeNode.BLACK

    def _delete_min(self, h):
        if h.left is None:
            return None

        if not self.is_red(h.left) and not self.is_red(h.left.left):
            h = self.move_red_left(h)

        h.left = self._delete_min(h.left)
        return self.balance(h)

    def balance(self, h):
        if self.is_red(h.right):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        return h

    def check(self):
        assert(self.is23())
        assert(self.is_balanced())

    def is23(self):
        return self._is23(self._root)

    def _is23(self, node):
        if node is None:
            return True
        if self.is_red(node.right):
            return False
        if self.is_red(node.left) and self.is_red(node.left.left):
            return False
        return self._is23(node.left) and self._is23(node.right)

    def is_balanced(self):
        black = 0
        node = self._root
        while node is not None:
            if not self.is_red(node):
                black += 1
            node = node.left

        return self._is_balanced(self._root, black)

    def _is_balanced(self, node, black):
        if node is None:
            return black == 0
        if not self.is_red(node):
            black -= 1
        return self._is_balanced(node.left, black) and self._is_balanced(node.right, black)


def test_rb_tree1(count):
    keys = [i for i in range(count)]
    rbtree = RBTree()
    for key in keys:
        rbtree.put(key, key*key)

    for key in keys:
        assert(rbtree.get(key) == key*key)


def test_rb_tree2(count):
    keys = [i for i in range(count)]
    random.shuffle(keys)

    rbtree = RBTree()
    for key in keys:
        rbtree.put(key, key*key)

    for key in keys:
        assert(rbtree.get(key) == key*key)


def test_rb_tree3(count):
    keys = [i for i in range(count)]
    random.shuffle(keys)

    rbtree = RBTree()
    for key in keys:
        rbtree.put(key, key*key)

    for key in keys:
        assert(rbtree.get(key) == key*key)

    random.shuffle(keys)
    for key in keys:
        keys.remove(key)
        rbtree.delete(key)
        assert(rbtree.get(key) is None)
        for k in keys:
            assert(rbtree.get(k) == k*k)


if __name__ == '__main__':
    test_rb_tree1(100)
    test_rb_tree2(100)
    test_rb_tree3(20)
    print('done')
