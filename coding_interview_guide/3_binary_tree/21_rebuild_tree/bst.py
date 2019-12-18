import operator


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST():
    def __init__(self, root=None):
        self.root = root

    def __eq__(self, rhs):
        def recursive(lhs, rhs):
            if lhs is None:
                return rhs is None

            if rhs is None:
                return lhs is None

            if lhs.val != rhs.val:
                return False

            return recursive(lhs.left, rhs.left) and recursive(
                    lhs.right, rhs.right)

        return recursive(self.root, rhs.root)

    def insert_recursive(self, val):
        def recursive(node, val):
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = recursive(node.left, val)
            elif val > node.val:
                node.right = recursive(node.right, val)

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


def rebuild_tree_by_pre_in_order(pre_order, in_order):
    def rebuild(pre_beg, pre_end, in_beg, in_end):
        if pre_beg >= pre_end:
            return None

        root_val = pre_order[pre_beg]
        root = TreeNode(root_val)
        index = index_of_inorder[root_val]
        root.left = rebuild(pre_beg+1, pre_beg+index-in_beg+1, in_beg, index)
        root.right = rebuild(pre_beg+index-in_beg+1, pre_end, index+1, in_end)
        return root

    if not pre_order or not in_order:
        return None

    index_of_inorder = {v: k for k, v in enumerate(in_order)}
    return rebuild(0, len(pre_order), 0, len(in_order))


def rebuild_tree_by_in_post_order(in_order, post_order):
    def rebuild(in_beg, in_end, post_beg, post_end):
        if in_beg >= in_end:
            return None

        root_val = post_order[post_end-1]
        root = TreeNode(root_val)
        index = index_of_inorder[root_val]
        root.left = rebuild(in_beg, index, post_beg, post_beg+index-in_beg)
        root.right = rebuild(index+1, in_end,
                             post_beg+index-in_beg, post_end-1)
        return root

    index_of_inorder = {v: k for k, v in enumerate(in_order)}
    return rebuild(0, len(in_order), 0, len(post_order))


def rebuild_tree_by_pre_post_order(pre_order, post_order):
    def rebuild(pre_beg, pre_end, post_beg, post_end):
        root_val = pre_order[pre_beg]
        root = TreeNode(root_val)

        if pre_beg + 1 == pre_end:
            return root

        v = pre_order[pre_beg+1]
        index = index_of_post_order[v]
        root.left = rebuild(pre_beg+1, pre_beg+index-post_beg+2,
                            post_beg, index+1)
        root.right = rebuild(pre_beg+index-post_beg+2, pre_end,
                             index+1, post_end-1)
        return root

    index_of_post_order = {v: k for k, v in enumerate(post_order)}
    return rebuild(0, len(pre_order), 0, len(post_order))


def make_cbt(count):
    if count == 0:
        return None

    nodes = [TreeNode(i) for i in range(count)]
    for i in range(count):
        left = 2*i + 1
        right = 2*i + 2
        if left < count:
            nodes[i].left = nodes[left]
        if right < count:
            nodes[i].right = nodes[right]

    return nodes[0]


def test():
    r = make_cbt(99)
    tree = BST(r)

    pre_order = tree.preorder_traversal_recursive()
    in_order = tree.inorder_traversal_recursive()
    post_order = tree.postorder_traversal_recursive()

    r = rebuild_tree_by_pre_post_order(pre_order, post_order)
    tree_rebuild = BST(r)
    pre_rebuild = tree_rebuild.preorder_traversal_recursive()
    in_rebuild = tree_rebuild.inorder_traversal_recursive()
    post_rebuild = tree_rebuild.postorder_traversal_recursive()

    if not tree == tree_rebuild:
        raise Exception('error')

    if not operator.eq(pre_order, pre_rebuild):
        raise Exception('ERROR')
    if not operator.eq(in_order, in_rebuild):
        raise Exception('ERROR')
    if not operator.eq(post_order, post_rebuild):
        raise Exception('ERROR')


if __name__ == '__main__':
    test()
