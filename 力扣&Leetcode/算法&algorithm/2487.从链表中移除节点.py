# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pin = head
        tail = None
        while pin:
            tmp = pin.next
            pin.next = tail
            tail = pin
            pin = tmp
            # print(tail)
        pin = tail
        while pin.next:
            if pin.val <= pin.next.val:
                pin = pin.next
            else:
                pin.next = pin.next.next
        pin = tail
        prev = None
        while pin:
            tmp = pin.next
            pin.next = prev
            prev = pin
            pin = tmp
        return prev
