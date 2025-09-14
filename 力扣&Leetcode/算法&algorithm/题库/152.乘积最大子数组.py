class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi = mx = 1
        ans = -float("inf")
        for i in nums:
            if i < 0:
                mi, mx = mx, mi
            mi = min(i * mi, i)
            mx = max(i * mx, i)
            ans = max(ans, mx)
        return ans
