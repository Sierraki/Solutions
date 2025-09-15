# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # [] or not
        if not head:
            return None
        # cope head
        while head and head.val == val:
            head = head.next
        # re [] or not
        if not head:
            return None
        # cope after
        pin = head
        while pin.next:
            if pin.next.val == val:  # jump
                pin.next = pin.next.next
            else:
                pin = pin.next
        return head
