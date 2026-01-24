# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        a = []
        pin = head
        while pin:
            a.append(pin.val)
            pin = pin.next
        a.sort()
        dummy = ListNode()
        pin = dummy
        for i in a:
            pin.next = ListNode(i)
            pin = pin.next
        return dummy.next
