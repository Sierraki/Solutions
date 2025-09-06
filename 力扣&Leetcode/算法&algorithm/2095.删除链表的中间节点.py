# 常规做法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        pin = head
        while pin:
            n += 1
            pin = pin.next
        tar = n // 2
        if n == 1:
            return None
        a = 0
        pin = head
        while pin:
            if a == tar - 1:
                if pin.next.next:
                    pin.next = pin.next.next
                else:
                    pin.next = None
                break
            a += 1
            pin = pin.next
        return head
# 快慢指针
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        if not slow.next:
            return None
        fast = head.next
        while head:
            if not fast.next or not fast.next.next:
                break
            fast = fast.next.next
            slow = slow.next
        if not slow.next.next:
            slow.next = None
        else:
            slow.next = slow.next.next
        return head
