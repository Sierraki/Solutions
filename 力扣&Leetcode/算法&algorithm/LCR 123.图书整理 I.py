# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        a = []
        pin = head
        while pin:
            a.append(pin.val)
            pin = pin.next
        return a[::-1]
