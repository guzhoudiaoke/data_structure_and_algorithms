class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BST():
    def __init__(self, root=None):
        self.root = root

    def insert_recursive(self, val):
        def recursive(node, val):
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = recursive(node.left, val)
                node.left.parent = node
            elif val > node.val:
                node.right = recursive(node.right, val)
                node.right.parent = node

            return node

        self.root = recursive(self.root, val)

    def print_tree(self):
        def preorder(node):
            if not node:
                return '#'

            s = str(node.val)
            if node.left or node.right:
                s += '('
                s += preorder(node.left)
                s += ', '
                s += preorder(node.right)
                s += ')'

            return s

        return preorder(self.root)

    def serialize(self):
        def preorder(node):
            if not node:
                return '#|'

            res = str(node.val) + '|'
            res += preorder(node.left)
            res += preorder(node.right)
            return res

        return preorder(self.root)

    def deserialize(self, pre_order_str):
        def reconstruct(q):
            s = q.pop(0)
            if s == '#':
                return None

            node = TreeNode(int(s))
            node.left = reconstruct(q)
            node.right = reconstruct(q)
            return node

        q = pre_order_str.split('|')
        self.root = reconstruct(q)

    def serialize_by_level(self):
        if not self.root:
            return '#|'

        s = str(self.root.val) + '|'
        q = [self.root]
        while q:
            node = q.pop(0)
            if node.left is not None:
                s += str(node.left.val) + '|'
                q.append(node.left)
            else:
                s += '#|'
            if node.right is not None:
                s += str(node.right.val) + '|'
                q.append(node.right)
            else:
                s += '#|'

        return s

    def deserialize_by_level(self, level_str):
        def build_node(s):
            if s == '#':
                return None
            return TreeNode(int(s))

        if not level_str:
            self.root = None
            return

        splits = level_str.split('|')
        root = build_node(splits.pop(0))
        if root is None:
            return

        q = [root]
        while q:
            node = q.pop(0)
            node.left = build_node(splits.pop(0))
            if node.left is not None:
                q.append(node.left)

            node.right = build_node(splits.pop(0))
            if node.right is not None:
                q.append(node.right)

        self.root = root
