class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        nums = timeSeries
        n = len(nums)
        res = 0
        for i in range(n - 1):
            if nums[i] + duration - 1 < nums[i + 1]:
                a = duration
            elif nums[i] + duration - 1 >= nums[i + 1]:
                a = nums[i + 1] - nums[i]
            res = res + a
        return res + duration
