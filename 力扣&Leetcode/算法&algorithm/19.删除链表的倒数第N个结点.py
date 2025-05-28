# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pin = head
        len = 0
        while pin:
            len += 1
            pin = pin.next
        tar = len - n

        if tar == 0:
            if len > 1:
                return head.next
            else:
                return None
        else:
            pin = head
            while tar - 1 > 0 and pin.next:
                tar -= 1
                pin = pin.next
            pin.next = pin.next.next
            # print(len)
            return head
