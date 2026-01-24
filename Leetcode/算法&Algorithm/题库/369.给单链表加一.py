# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        pin = head
        while pin:
            a.append(str(pin.val))
            pin = pin.next
        res = "".join(a)
        res = str(int(res) + 1)
        dummy = ListNode()
        pin = dummy
        for i in res:
            pin.next = ListNode(int(i))
            pin = pin.next
        return dummy.next
