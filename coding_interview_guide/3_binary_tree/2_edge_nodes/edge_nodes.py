class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def height(node, level):
    if node is None:
        return level
    return max(height(node.left, level+1), height(node.right, level+1))


def get_edge_nodes1(root):
    def set_edge_map(node, level):
        if node is None:
            return

        if (level, 'left') not in edge_map:
            edge_map[(level, 'left')] = node
        edge_map[(level, 'right')] = node
        set_edge_map(node.left, level+1)
        set_edge_map(node.right, level+1)

    def get_leaf_nodes_not_in_map(node, level):
        if node is None:
            return
        if node.is_leaf() and (node != edge_map[(level, 'left')] and
           node != edge_map[(level, 'right')]):
            result.append(node.val)

        get_leaf_nodes_not_in_map(node.left, level+1)
        get_leaf_nodes_not_in_map(node.right, level+1)

    result = []
    if root is None:
        return result

    max_level = height(root, 0)
    edge_map = {}
    set_edge_map(root, 0)

    # left edge nodes
    for level in range(max_level):
        result.append(edge_map[(level, 'left')].val)

    # leaf nodes
    get_leaf_nodes_not_in_map(root, 0)

    # right edge nodes
    for level in reversed(range(max_level)):
        if edge_map[(level, 'right')] != edge_map[(level, 'left')]:
            result.append(edge_map[(level, 'right')].val)

    return result


def get_edge_nodes2(root):
    def get_left_edge(node, flag):
        if node is None:
            return

        if flag or node.is_leaf():
            result.append(node.val)

        get_left_edge(node.left, flag)
        get_left_edge(node.right, flag and node.left is None)

    def get_right_edge(node, flag):
        if node is None:
            return

        get_right_edge(node.left, flag and node.right is None)
        get_right_edge(node.right, flag)

        if flag or node.is_leaf():
            result.append(node.val)

    if root is None:
        return

    result = [root.val]
    if root.left is not None and root.right is not None:
        get_left_edge(root.left, True)
        get_right_edge(root.right, True)
    else:
        node = root.left if root.left is not None else root.right
        get_edge_nodes2(node)

    return result


def test_get_edge_nodes():
    nodes = [TreeNode(i) for i in range(17)]
    root = nodes[1]
    nodes[1].left, nodes[1].right = nodes[2], nodes[3]
    nodes[2].right = nodes[4]
    nodes[4].left, nodes[4].right = nodes[7], nodes[8]
    nodes[8].right = nodes[11]
    nodes[11].left, nodes[11].right = nodes[13], nodes[14]

    nodes[3].left, nodes[3].right = nodes[5], nodes[6]
    nodes[5].left, nodes[5].right = nodes[9], nodes[10]
    nodes[9].left = nodes[12]
    nodes[12].left, nodes[12].right = nodes[15], nodes[16]

    result1 = get_edge_nodes1(root)
    print(result1)

    result2 = get_edge_nodes2(root)
    print(result2)


if __name__ == '__main__':
    test_get_edge_nodes()
