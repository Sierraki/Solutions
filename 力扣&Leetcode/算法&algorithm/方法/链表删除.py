def remove_node(head, target_val):
    # 如果头节点为空
    if not head:
        return None
    # 如果头节点是要删除的节点
    while head and head.val == target_val:
        head = head.next
    # 如果整个链表都被删除了
    if not head:
        return None
    current = head
    while current.next:
        if current.next.val == target_val:
            current.next = current.next.next  # 跳过目标节点
        else:
            current = current.next  # 继续往后走
    return head
