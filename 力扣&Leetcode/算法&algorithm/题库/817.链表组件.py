# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        cnt = set(nums)
        res = []
        pin = head
        while pin:
            res.append(pin.val)
            pin = pin.next
        for i, j in enumerate(res):
            if j in cnt:
                res[i] = "T"
            else:
                res[i] = "F"
        ans = ("".join(res)).split("F")
        ans1 = 0
        for i in ans:
            if i != "":
                ans1 += 1
        return ans1
