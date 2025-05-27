class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)
