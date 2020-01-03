class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_length_path_with_sum(root, sum):
    def pre_order(node, pre_sum, level, max_len):
        if node is None:
            return max_len

        cur_sum = pre_sum + node.val
        if cur_sum not in sum_map:
            sum_map[cur_sum] = level

        if cur_sum-sum in sum_map:
            max_len = max(max_len, level-sum_map[cur_sum-sum])

        max_len = pre_order(node.left, cur_sum, level+1, max_len)
        max_len = pre_order(node.right, cur_sum, level+1, max_len)

        if sum_map[cur_sum] == level:
            sum_map.pop(cur_sum)

        return max_len

    sum_map = {0: 0}
    return pre_order(root, pre_sum=0, level=0, max_len=0)


def test_max_length_path_with_sum():
    vals = [-3, 3, -9, 1, 0, 2, 1, 1, 6]
    nodes = [TreeNode(v) for v in vals]

    root = nodes[0]
    nodes[0].left, nodes[0].right = nodes[1], nodes[2]
    nodes[1].left, nodes[1].right = nodes[3], nodes[4]
    nodes[2].left, nodes[2].right = nodes[5], nodes[6]
    nodes[4].left, nodes[4].right = nodes[7], nodes[8]

    result1 = max_length_path_with_sum(root, 6)
    print(result1)
    result2 = max_length_path_with_sum(root, -9)
    print(result2)
    result3 = max_length_path_with_sum(root, -10)
    print(result3)
    result4 = max_length_path_with_sum(root, -11)
    print(result4)
    result5 = max_length_path_with_sum(root, 4)
    print(result5)
    result6 = max_length_path_with_sum(root, 1)
    print(result6)


if __name__ == '__main__':
    test_max_length_path_with_sum()
