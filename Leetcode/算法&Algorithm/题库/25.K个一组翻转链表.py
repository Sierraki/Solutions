# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = []
        pin = head
        cur = []
        while pin:
            tmp = pin.next
            pin.next = None
            cur.append(pin)
            if len(cur) == k:
                res.append(cur)
                cur = []
            pin = tmp
        if len(cur) > 0:
            res.append(cur)
        for i, j in enumerate(res):
            if len(j) == k:
                res[i] = j[::-1]
        nums = [j for i in res for j in i]
        dummy = ListNode()
        pin = dummy
        for i in nums:
            pin.next = i
            pin = pin.next
        return dummy.next
