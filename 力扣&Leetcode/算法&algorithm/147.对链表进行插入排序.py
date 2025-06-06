# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        dummy.next = head
        pin = dummy
        while pin.next:
            if pin.val > pin.next.val:
                new = pin.next
                pin.next = pin.next.next
                p1 = dummy
                while p1.next:
                    if p1.val <= new.val <= p1.next.val:
                        new.next = p1.next
                        p1.next = new
                        break
                    p1 = p1.next
            else:
                pin = pin.next
        return dummy.next
