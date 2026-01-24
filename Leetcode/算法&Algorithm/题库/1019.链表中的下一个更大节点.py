# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        pin = head
        while pin:
            nums.append(pin.val)
            pin = pin.next
        n = len(nums)
        ans = [0] * n
        index = []
        for i, j in enumerate(nums):
            index.append([i, j])
        res = []
        while index:
            cur = index[0]
            del index[0]
            if not res:
                res.append(cur)
            else:
                while res and res[-1][1] < cur[1]:
                    ans[res[-1][0]] = cur[1]
                    res.pop()
                res.append(cur)
        return ans
