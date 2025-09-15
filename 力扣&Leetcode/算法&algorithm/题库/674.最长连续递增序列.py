class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur = 1
        maxx = 1

        left = 0

        n = len(nums)

        for i in range(1, n):
            if nums[i] - nums[i - 1] > 0:
                cur += 1
                if cur >= maxx:
                    maxx = cur
            if nums[i] - nums[i - 1] <= 0:
                cur = 1
        return maxx
