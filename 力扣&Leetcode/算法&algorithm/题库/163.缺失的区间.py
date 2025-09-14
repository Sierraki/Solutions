class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        nums = [i for i in nums if lower <= i <= upper]
        res = []
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                a = [nums[i - 1] + 1, nums[i] - 1]
                res.append(a)
        return res
