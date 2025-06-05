# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        res = []
        pin = head
        if not pin.next.next:
            return [-1, -1]
        while pin.next.next:
            n += 1
            if pin.next.val > pin.val and pin.next.val > pin.next.next.val:
                res.append(n)
            if pin.next.val < pin.val and pin.next.val < pin.next.next.val:
                res.append(n)
            pin = pin.next
        # print(res)
        res.sort()
        if len(res) < 2:
            return [-1, -1]
        mx = res[-1] - res[0]
        mi = float("inf")
        for i in range(1, len(res)):
            mi = min(mi, res[i] - res[i - 1])
        return [mi, mx]
