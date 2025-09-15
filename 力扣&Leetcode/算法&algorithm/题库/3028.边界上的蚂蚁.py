class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s = ans = 0
        for i in nums:
            s += i
            if s == 0:
                ans += 1
        return ans
