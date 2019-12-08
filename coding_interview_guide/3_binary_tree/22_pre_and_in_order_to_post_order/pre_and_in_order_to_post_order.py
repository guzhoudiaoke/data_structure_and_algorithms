def pre_order_in_order_to_post_order1(preorder, inorder):
    def get_post_order(preorder, inorder):
        if not preorder or not inorder:
            return []

        root = preorder[0]
        index = inorder.index(root)

        left = get_post_order(preorder[1:index+1], inorder[:index])
        right = get_post_order(preorder[index+1:], inorder[index+1:])
        return left + right + [root]

    if len(preorder) != len(inorder):
        raise Exception('Error')

    return get_post_order(preorder, inorder)


def pre_order_in_order_to_post_order2(preorder, inorder):
    def get_post_order(pre_beg, pre_end, in_beg, in_end):
        if pre_beg >= pre_end or in_beg >= in_end:
            return []

        root = preorder[pre_beg]
        index = index_of_inorder[root]

        left = get_post_order(pre_beg+1, pre_beg+index-in_beg+1, in_beg, index)
        right = get_post_order(pre_beg+index-in_beg+1, pre_end,
                               index+1, in_end)
        return left + right + [root]

    if len(preorder) != len(inorder):
        return None

    index_of_inorder = {v: k for k, v in enumerate(inorder)}
    return get_post_order(0, len(preorder), 0, len(inorder))


def pre_order_in_order_to_post_order3(preorder, inorder):
    def get_post_order(pre_beg, pre_end, in_beg, in_end):
        if pre_end - pre_beg != in_end - in_beg:
            raise Exception('Error index')

        if pre_beg >= pre_end:
            return []

        if pre_end - pre_beg == 1:
            return [preorder[pre_beg]]

        root = preorder[pre_beg]
        index = index_of_inorder[root]

        left = get_post_order(pre_beg+1, pre_beg+index-in_beg+1, in_beg, index)
        right = get_post_order(pre_beg+index-in_beg+1, pre_end,
                               index+1, in_end)
        return left + right + [root]

    if len(preorder) != len(inorder):
        return None

    index_of_inorder = {v: k for k, v in enumerate(inorder)}
    return get_post_order(0, len(preorder), 0, len(inorder))
