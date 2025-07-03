class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)  # 先复制
        current = current.next  # 再移动
    return head


# 创建两个链表
l1 = build_linked_list([1, 2, 4, 56, 8, 6, 8, 9, 9, 8])
l2 = build_linked_list([1, 3, 4])


# 打印链表（用于测试）
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


print("链表 l1:")
print_linked_list(l1)

print("链表 l2:")
print_linked_list(l2)
