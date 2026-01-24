# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        pin = head
        while pin:
            tmp = pin.next
            pin.next = pre
            pre = pin
            pin = tmp
        return pre
