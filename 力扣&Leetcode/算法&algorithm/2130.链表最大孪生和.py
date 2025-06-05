# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        pin = head
        n = 0
        while pin:
            a.append(pin.val)
            pin = pin.next
            n += 1
        cnt = n // 2
        mx = 0
        while cnt > 0:
            cnt -= 1
            mx = max(mx, (a[0] + a[-1]))
            del a[0]
            del a[-1]
        return mx
