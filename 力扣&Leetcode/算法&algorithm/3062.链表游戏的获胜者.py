# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        Odd = Even = 0
        pin = head
        while pin:
            res = max(pin.val, pin.next.val)
            if res % 2 == 0:
                Even += 1
            else:
                Odd += 1
            pin = pin.next.next

        if Even == Odd:
            return "Tie"
        else:
            if Even > Odd:
                return "Even"
            else:
                return "Odd"
