class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lens = len(nums)
        tag = lens * (lens + 1) / 2
        s = 0
        for i in nums:
            s = s + i
        return int(tag - s)
