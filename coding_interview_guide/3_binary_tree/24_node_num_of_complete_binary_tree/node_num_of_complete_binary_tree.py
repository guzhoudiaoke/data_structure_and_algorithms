class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def node_num_of_cbt2(root):
    def most_left_level(node, level):
        while node:
            level += 1
            node = node.left
        return level - 1

    def node_num(node, level):
        if level == height:
            return 1

        if most_left_level(node.right, level+1) == height:
            return (1 << (height - level)) + node_num(node.right, level+1)
        else:
            return (1 << (height - level - 1)) + node_num(node.left, level+1)

    if root is None:
        return 0

    height = most_left_level(root, 1)
    return node_num(root, 1)


def node_num_of_cbt(root):
    def most_left_level(node, level):
        while node:
            level += 1
            node = node.left
        return level - 1

    def node_num(node, level):
        if level == height:
            return 1

        if most_left_level(node.right, level+1) == height:
            return 2 ** (height-level) + node_num(node.right, level+1)
        else:
            return 2 ** (height-level-1) + node_num(node.left, level+1)

    if root is None:
        return 0

    height = most_left_level(root, 0)
    return node_num(root, 0)
