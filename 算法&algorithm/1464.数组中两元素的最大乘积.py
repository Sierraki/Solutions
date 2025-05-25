class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if len(nums) >= 2:
            return (nums[0] - 1) * (nums[1] - 1)
        else:
            return 0
