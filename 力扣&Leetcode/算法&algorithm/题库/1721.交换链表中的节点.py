# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pin = head
        for _ in range(k - 1):
            pin = pin.next
        pin1 = pin
        pin2 = head
        while pin.next:
            pin = pin.next
            pin2 = pin2.next
        pin1.val, pin2.val = pin2.val, pin1.val
        return head
