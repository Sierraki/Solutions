# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pin = head
        tail = None
        while pin:
            tmp = pin.next
            pin.next = tail
            tail = pin
            pin = tmp
            # print(tail)
        return tail
