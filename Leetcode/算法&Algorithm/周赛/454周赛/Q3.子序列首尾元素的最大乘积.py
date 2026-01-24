class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ans = -float("inf")
        mx = -float("inf")
        mi = float("inf")
        for i in range(m - 1, len(nums)):
            mi = min(mi, nums[i - (m - 1)])
            mx = max(mx, nums[i - (m - 1)])
            ans = max(ans, nums[i] * mx, nums[i] * mi)
        return ans
