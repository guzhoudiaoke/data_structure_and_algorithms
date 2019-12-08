class TreeNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def __eq__(self, rhs):
        def recursive(lhs, rhs):
            if lhs is None:
                return rhs is None
            if rhs is None:
                return lhs is None

            if lhs.key != rhs.key or lhs.val != rhs.val:
                return False
            l_eq = recursive(lhs.left, rhs.left)
            r_eq = recursive(lhs.right, rhs.right)
            return l_eq and r_eq

        return recursive(self.root, rhs.root)

    def insert_recursive(self, key, val):
        def recursive(node, key, val):
            if not node:
                return TreeNode(key, val)

            if key < node.key:
                node.left = recursive(node.left, key, val)
            elif key > node.key:
                node.right = recursive(node.right, key, val)
            return node

        self.root = recursive(self.root, key, val)

    def insert_non_recursive(self, key, val):
        node = TreeNode(key, val)
        if not self.root:
            self.root = node
            return

        parent = None
        cur = self.root
        while cur:
            parent = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                cur.val = val
                return

        if key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def inorder_traversal_recursive(self):
        def recursive(node):
            if node:
                recursive(node.left)
                result.append(node.key)
                recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def inorder_traversal_non_recursive(self):
        result = []
        if not self.root:
            return result

        node = self.root
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.key)
                node = node.right

        return result

    def preorder_traversal_recursive(self):
        def recursive(node):
            if node:
                result.append(node.key)
                recursive(node.left)
                recursive(node.right)

        result = []
        recursive(self.root)
        return result

    def preorder_traversal_non_recursive(self):
        result = []
        if not self.root:
            return result

        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.key)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def postorder_traversal_recursive(self):
        def recursive(node):
            if node:
                recursive(node.left)
                recursive(node.right)
                result.append(node.key)

        result = []
        recursive(self.root)
        return result

    def postorder_traversal_non_recursive1(self):
        result = []
        if not self.root:
            return result

        stack1 = [self.root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            result.append(stack2.pop().key)

        return result

    def postorder_traversal_non_recursive2(self):
        result = []
        if not self.root:
            return result

        stack = [self.root]
        flag = self.root
        while stack:
            node = stack[-1]
            if node.left and node.left != flag and node.right != flag:
                stack.append(node.left)
            elif node.right and node.right != flag:
                stack.append(node.right)
            else:
                result.append(stack.pop().key)
                flag = node

        return result

    def is_balance(self):
        def check(node):
            if node is None:
                return 0, True

            left_height, left_balance = check(node.left)
            if not left_balance:
                return 0, False

            right_height, right_balance = check(node.right)
            if not right_balance:
                return 0, False

            if abs(left_height-right_height) > 1:
                return 0, False

            return max(left_height, right_height)+1, True

        height, balance = check(self.root)
        return balance

    def is_bst(self):
        def check(node, minnode, maxnode):
            if node is None:
                return True

            if maxnode and node.key >= maxnode.key:
                return False
            if minnode and node.key <= minnode.key:
                return False

            if not check(node.left, minnode, node):
                return False
            if not check(node.right, node, maxnode):
                return False

            return True

        return check(self.root, None, None)

    def generate_by_sorted_array(self, arr):
        def generate(arr):
            if not arr:
                return None

            mid = len(arr) // 2
            root = TreeNode(arr[mid], arr[mid])
            root.left = generate(arr[:mid])
            root.right = generate(arr[mid+1:])

            return root

        self.root = generate(arr)
