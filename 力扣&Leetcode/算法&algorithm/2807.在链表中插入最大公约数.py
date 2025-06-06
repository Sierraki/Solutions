# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        def check(a, b):
            tar = min(a, b)
            last = 1
            for i in range(2, tar + 1):
                if a % i == 0 and b % i == 0:
                    last = i
            return last

        pin = head
        while pin.next:
            new = ListNode(check(pin.val, pin.next.val))
            new.next = pin.next
            pin.next = new
            pin = pin.next.next
        return head
