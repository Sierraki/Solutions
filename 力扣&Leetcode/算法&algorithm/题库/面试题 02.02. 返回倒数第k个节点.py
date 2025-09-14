# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        n = 0
        pin = head
        while pin:
            n += 1
            pin = pin.next
        print(n)
        tar = n - k
        pin = head
        while tar > 0:
            tar -= 1
            pin = pin.next
        return pin.val
