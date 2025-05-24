# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = Counter()
        current = head
        while current:
            if current.val not in cnt:
                cnt[current.val] += 1
                prev = current  # 保留前驱节点
            else:
                prev.next = current.next  # 跳过当前节点
            current = current.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        while head.next and head.val == head.next.val:
            head = head.next
        cnt = Counter()
        pin = head
        while pin.next:
            if pin.next.val not in cnt:
                cnt[pin.next.val] = 1
                pin = pin.next
            else:
                pin.next = pin.next.next
        return head
