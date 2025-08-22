class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        mi = float("inf")
        for i in range(1, len(nums)):
            mi = min(mi, abs(nums[i] - nums[i - 1]))
        return mi
