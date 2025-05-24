# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        cnt = Counter(nums)
        # 处理头节点是待删除的情况
        while head and head.val in cnt:
            head = head.next
        if not head:
            return None
        # 保留头节点，用于遍历后续节点
        current = head
        while current.next:
            if current.next.val in cnt:
                # 跳过下一个节点
                current.next = current.next.next
            else:
                # 移动到下一个节点
                current = current.next
        return head
