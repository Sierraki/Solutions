class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l = float("inf")
        mx = -float("inf")
        for i in range(1, len(nums)):
            l = min(l, nums[i - 1])
            if nums[i] > l:
                mx = max(mx, nums[i] - l)
        if mx == -float("inf"):
            return -1
        return mx
