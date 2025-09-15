class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        res = float("inf")
        for _ in range(n // 2):
            res = min(res, (nums[0] + nums[-1]) / 2)
            del nums[0]
            nums.pop()
        return res
