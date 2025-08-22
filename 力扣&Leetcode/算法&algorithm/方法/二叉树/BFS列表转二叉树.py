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


# 加入None
def level_order_with_none(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_list = []
        # 标记这一层是否全是 None，用于后续优化
        is_all_none = True

        for _ in range(len(queue)):
            node = queue.popleft()

            if node:
                level_list.append(node.val)
                is_all_none = False
                # 无论子节点是否存在，都将其添加到队列
                queue.append(node.left)
                queue.append(node.right)
            else:
                level_list.append(None)
                # None 节点没有子节点，所以这里不需要再添加到队列

        # 如果这一层不是全 None，才添加到结果中
        if not is_all_none:
            result.append(level_list)

    return result
