class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum([int(j) for i in nums for j in str(i)]))
