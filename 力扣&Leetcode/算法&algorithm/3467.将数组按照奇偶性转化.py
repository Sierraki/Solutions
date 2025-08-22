class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = 0
        for i in nums:
            if i % 2 == 1:
                odd += 1
        even = len(nums) - odd
        return [0] * even + [1] * odd
