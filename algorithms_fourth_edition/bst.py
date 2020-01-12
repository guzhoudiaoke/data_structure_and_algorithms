import random


class TreeNode():
    def __init__(self, key, val, left=None, right=None, size=0):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.size = size


class BinarySearchTree():
    def __init__(self):
        """ Initializes an empty symbol table.
        """
        self.root = None

    def is_empty(self):
        """ Returns True if this BST is empty.
        return True if this BST is empty; False otherwise
        """
        return self.size() == 0

    def _size(self, node):
        return node.size if node is not None else 0

    def size(self):
        """ Returns the number of key-value pairs in this BST.
        return the number of key-value pairs in this BST
        """
        return self._size(self.root)

    def contain(self, key):
        """ Does this symbol table contain the given key?
        """
        if key is None:
            raise Exception('argument is None')
        return self.get(key) is not None

    def _put(self, node, key, val):
        if node is None:
            return TreeNode(key, val, size=1)

        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val

        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def put(self, key, val):
        """ Inserts the specified key-value pair into the BST,
        overwriting the old value with the new value if the BST already
        contains the specified key.
        Deletes the specified key (and its associated value) from this BST
        if the specified value is None
        """
        if key is None:
            raise Exception('key is None')
        if val is None:
            self.delete(key)
            return

        self.root = self._put(self.root, key, val)
        assert(self.check())

    def _get(self, node, key):
        if node is None:
            return None

        if key < node.key:
            return self._get(node.left, key)
        if key > node.key:
            return self._get(node.right, key)

        return node.val

    def get(self, key):
        """ Returns the value associated with the given key.
        """
        if key is None:
            raise Exception('calls get() with a None key')
        return self._get(self.root, key)

    def _inorder(self, node, result):
        if node is None:
            return

        self._inorder(node.left, result)
        result.append((node.key, node.val))
        self._inorder(node.right, result)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def min(self):
        if self.is_empty():
            raise Exception('calls min() with empty bst')
        return self._min(self.root).key

    def _max(self, node):
        if node.right is None:
            return node
        return self._max(node.right)

    def max(self):
        if self.is_empty():
            raise Exception('calls max() with empty bst')
        return self._max(self.root).key

    def _delete_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._delete_min(node.left)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_min(self):
        """ Removes the smallest key and associated value from the BST.
        """
        if self.is_empty():
            raise Exception('bst under flow')
        self.root = self._delete_min(self.root)
        assert(self.check())

    def _delete_max(self, node):
        if node.right is None:
            return node.left

        node.right = self._delete_max(node.right)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_max(self):
        """ Removes the largest key and associated value from the BST.
        """
        if self.is_empty():
            raise Exception('bst under flow')
        self.root = self._delete_max(self.root)
        assert(self.check())

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            t = node
            node = self._min(t.right)
            node.right = self._delete_min(t.right)
            node.left = t.left

        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete(self, key):
        """Removes the specified key and its associated value from this BST
        (if the key is in this BST).
        """
        if key is None:
            raise Exception('calls delete() with a None key')
        self.root = self._delete(self.root, key)
        assert(self.check())

    def _select(self, node, k):
        if node is None:
            return None
        t = self._size(node.left)
        if t > k:
            return self._select(node.left, k)
        if t < k:
            return self._select(node.right, k-t-1)
        return node

    def select(self, k):
        """ Return the key in the symbol table whose rank is k.
        This is the (k+1)st smallest key in the BST.
        """
        if k < 0 or k >= self.size():
            raise Exception('argument to select() is invald')
        node = self._select(self.root, k)
        return node.key

    def _rank(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(node.left, key)
        if key > node.key:
            return 1 + self._size(node.left) + self._rank(node.right, key)
        return self._size(node.left)

    def rank(self, key):
        """ Return the number of keys in the symbol table strictly less than key
        """
        if key is None:
            raise Exception('argument to rank() is None')
        return self._rank(self.root, key)

    def _keys(self, node, q, lo, hi):
        if node is None:
            return
        if lo < node.key:
            self._keys(node.left, q, lo, hi)
        if lo <= node.key and node.key >= hi:
            q.append(node.key)
        if node.key > hi:
            self._keys(node.right, q, lo, hi)

    def keys(self, lo=None, hi=None):
        """ return all keys in the BST
        """
        if self.is_empty():
            return []
        if lo is None:
            lo = self.min()
        if hi is None:
            hi = self.max()

        q = []
        self._keys(self.root, q, lo, hi)
        return q

    def _floor(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._floor(node.left, key)
        t = self._floor(node.right, key)
        if t is not None:
            return t
        return node

    def floor(self, key):
        if key is None:
            raise Exception('argument to floor() is None')
        if self.is_empty():
            raise Exception('calls floor() with empty BST')
        node = self._floor(self.root, key)
        if node is None:
            raise Exception('argument to floor() is too small')
        return node.key

    def _floor2(self, node, key, best):
        if node is None:
            return best
        if key < node.key:
            return self._floor2(node.left, key, best)
        if key > node.key:
            return self._floor2(node.right, key, node.key)
        return node.key

    def floor2(self, key):
        if key is None:
            raise Exception('argument to floor() is None')
        if self.is_empty():
            raise Exception('calls floor() with empty BST')
        result = self._floor2(self.root, key, None)
        if result is None:
            raise Exception('argument to floor() is too small')
        return result

    def _ceiling(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            t = self._ceiling(node.left, key)
            if t is not None:
                return t
            return node
        return self._ceiling(node.right, key)

    def ceiling(self, key):
        if key is None:
            raise Exception('argument to ceiling() is None')
        if self.is_empty():
            raise Exception('calls ceiling() with empty BST')
        node = self._ceiling(self.root, key)
        if node is None:
            raise Exception('argument to ceiling() is too small')
        return node.key

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def height(self):
        return self._height(self.root)

    def _is_bst(self, node, mink, maxk):
        if node is None:
            return True
        if mink is not None and node.key <= mink:
            return False
        if maxk is not None and node.key >= maxk:
            return False
        return (self._is_bst(node.left, mink, node.key) and
                self._is_bst(node.right, node.key, maxk))

    def is_bst(self):
        return self._is_bst(self.root, None, None)

    def _is_size_consistent(self, node):
        if node is None:
            return True
        if node.size != self._size(node.left) + self._size(node.right) + 1:
            print(node.size, self._size(node.left), self._size(node.right))
            return False
        return (self._is_size_consistent(node.left) and
                self._is_size_consistent(node.right))

    def is_size_consistent(self):
        return self._is_size_consistent(self.root)

    def is_rank_consistent(self):
        for i in range(self.size()):
            if i != self.rank(self.select(i)):
                return False
        for key in self.keys():
            if key != self.select(self.rank(key)):
                return False
        return True

    def check(self):
        if not self.is_bst():
            print('Not bst')
        if not self.is_size_consistent():
            print('subtree counts not consistent')
        if not self.is_rank_consistent():
            print('ranks not consistent')

        return (self.is_bst() and
                self.is_size_consistent() and
                self.is_rank_consistent())


def test_binary_search_tree_put(count):
    keys = [i for i in range(count)]
    random.shuffle(keys)

    bst = BinarySearchTree()
    for k in keys:
        bst.put(k, 0)

    inorder = bst.inorder()
    print(inorder)


def test_binary_search_tree_get(count):
    keys = [i for i in range(count)]
    random.shuffle(keys)

    bst = BinarySearchTree()
    for k in keys:
        bst.put(k, k**2)

    inorder = bst.inorder()
    print(inorder)

    for k in keys:
        assert(bst.get(k) == k**2)


def test_binary_search_tree_delete(count):
    keys = [i for i in range(count)]
    random.shuffle(keys)

    bst = BinarySearchTree()
    for k in keys:
        bst.put(k, k**2)

    inorder = bst.inorder()
    print(inorder)

    random.shuffle(keys)
    for k in keys:
        bst.delete(k)
        inorder = bst.inorder()
        print('after delete', k, inorder)


def test_floor(count):
    keys = [i for i in range(count)]
    random.shuffle(keys)

    bst = BinarySearchTree()
    for k in keys:
        bst.put(k, 0)
        if bst.floor(k) != bst.floor2(k):
            raise Exception('floor() function inconsistent')

    print('done')


if __name__ == '__main__':
    test_binary_search_tree_put(10)
    test_binary_search_tree_get(10)
    test_binary_search_tree_delete(10)
    test_floor(10)
