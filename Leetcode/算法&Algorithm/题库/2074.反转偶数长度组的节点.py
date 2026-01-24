# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        pin = head
        res = []
        cur = []
        while pin:
            tmp = pin.next
            pin.next = None
            cur.append(pin)
            if len(cur) == n:
                if n % 2 == 0:
                    res.append(cur[::-1])
                else:
                    res.append(cur)
                cur = []
                n += 1
            pin = tmp
        if len(cur) > 0:
            if len(cur) % 2 == 0:
                res.append(cur[::-1])
            else:
                res.append(cur)
        nums = [j for i in res for j in i]
        dummy = ListNode()
        pin = dummy
        for i in nums:
            pin.next = i
            pin = pin.next
        return dummy.next
