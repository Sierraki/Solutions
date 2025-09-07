class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tar = nums[0]
        for i in range(1, len(nums)):
            tar &= nums[i]
        for num in nums:
            if num != tar:
                return 1
        return 0
