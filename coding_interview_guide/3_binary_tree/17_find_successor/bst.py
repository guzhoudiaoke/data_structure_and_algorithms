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

    def inorder_traversal_recursive(self):
        def recursive(node):
            if node:
                recursive(node.left)
                result.append(node.val)
                recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def preorder_traversal_recursive(self):
        def recursive(node):
            if node:
                result.append(node.val)
                recursive(node.left)
                recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def postorder_traversal_recursive(self):
        def recursive(node):
            if node:
                recursive(node.left)
                recursive(node.right)
                result.append(node.val)

        result = []
        recursive(self.root)
        return result

    def get_left_node(self, node):
        if node is None:
            return node

        while node.left is not None:
            node = node.left

        return node

    def successor(self, node):
        if node is None:
            return node

        if node.right is not None:
            return self.get_left_node(node.right)
        else:
            parent = node.parent
            while parent is not None and parent.left != node:
                node = parent
                parent = node.parent
            return parent
