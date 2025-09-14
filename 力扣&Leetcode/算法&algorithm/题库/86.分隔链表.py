# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = ListNode()  # <x
        l2 = ListNode()  # >=x
        p1 = l1
        p2 = l2
        pin = head
        while pin:
            if pin.val < x:
                p1.next = ListNode(pin.val)
                p1 = p1.next
            else:
                p2.next = ListNode(pin.val)
                p2 = p2.next
            pin = pin.next
        l2 = l2.next
        p1.next = l2
        return l1.next
