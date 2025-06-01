# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        n = 1
        pin = head
        while pin:
            n += 1
            pin = pin.next

        tar = n - cnt
        pin = head
        while tar > 1:
            pin = pin.next
            tar -= 1
        return pin
