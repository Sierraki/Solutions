# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast = head
        slow = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
            if not fast:
                return None
        slow = head
        while fast.next and slow.next:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
