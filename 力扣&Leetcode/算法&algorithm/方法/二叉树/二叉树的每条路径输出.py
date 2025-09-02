def fun(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]
    left=fun(root.left)
    right=fun(root.right)
    return [[root.val]+i for i in left+right]
