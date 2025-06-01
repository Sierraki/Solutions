# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainningPlan(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        pin = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                pin.next = ListNode(l1.val)
                l1 = l1.next
            else:
                pin.next = ListNode(l2.val)
                l2 = l2.next
            pin = pin.next
        pin.next = l1 or l2
        return dummy.next
