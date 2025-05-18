# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        b = "".join(map(str, a))
        return int(b, 2)
