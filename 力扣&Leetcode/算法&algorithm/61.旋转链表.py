# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        elif k == 0:
            return head
        len = 1
        pin = head
        while pin.next:
            len += 1
            pin = pin.next
        k = k % len
        if k == 0:
            return head
        tar = len - k
        pin = head
        # print(tar)
        while tar > 1:
            tar -= 1
            pin = pin.next
        # print(pin)
        tmp = pin.next
        # print(tmp)  # part 1
        pin.next = None
        # print(head)  # part 2
        pin = tmp
        while pin.next:
            pin = pin.next
        pin.next = head
        return tmp
