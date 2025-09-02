def cnt(root):
    if root is None:
        return 0
    left=cnt(root.left)
    right=cnt(root.right)
    return 1+max(left+right)