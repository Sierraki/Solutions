class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        nums = nums[::-1]
        pf = list(accumulate(nums))
        res = []
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] > pf[i - 1] / i:
                cnt += 1
        return cnt
