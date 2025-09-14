class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        tar = min(nums)
        for i in nums:
            if i < tar or i > tar + len(nums) - 1:
                return False
        if len(set(nums)) < len(nums):
            return False
        return True
