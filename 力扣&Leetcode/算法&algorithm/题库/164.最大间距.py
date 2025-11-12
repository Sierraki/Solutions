class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        for i in range(1, len(nums)):
            mx = max(mx, abs(nums[i] - nums[i - 1]))
        return mx
