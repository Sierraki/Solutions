# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        pin = head
        n = 0
        while pin:
            n += 1
            if n % 2 == 0:
                even.append(pin.val)
            else:
                odd.append(pin.val)
            pin = pin.next
        res = odd + even
        dummy = ListNode()
        pin = dummy
        for i in res:
            pin.next = ListNode(i)
            pin = pin.next
        return dummy.next
