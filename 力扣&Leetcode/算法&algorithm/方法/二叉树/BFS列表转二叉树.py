def build_tree_from_list(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    # 检查空列表和空根节点
    if not nodes or nodes[0] is None:
        return None
    root = TreeNode(nodes[0])
    res = deque([root])
    pin = 1
    while res and pin < len(nodes):
        cur = res.popleft()
        # 左节点
        if pin < len(nodes) and nodes[pin] != None:
            cur.left = TreeNode(nodes[pin])
            res.append(cur.left)
        pin += 1
        # 右节点
        if pin < len(nodes) and nodes[pin] != None:
            cur.right = TreeNode(nodes[pin])
            res.append(cur.right)
        pin += 1
    return root
