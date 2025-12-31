# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        res = []
        pin = head
        while pin:
            tmp = pin.next
            pin.next = None
            res.append(pin)
            pin = tmp
        ans = []
        l, r = 0, len(res) - 1
        while l <= r:
            ans.append(res[l])
            ans.append(res[r])
            l += 1
            r -= 1
        pin = ans[0]
        for i in range(1, len(res)):
            pin.next = ans[i]
            pin = pin.next

        """
        Do not return anything, modify head in-place instead.
        """
