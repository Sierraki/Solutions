class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = -float("inf")
        d = float("inf")
        for i in nums:
            if abs(i) < d:
                ans = i
                d = abs(i)
            elif abs(i) == d:
                if i > ans:
                    ans = i
        return ans
