class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            ans = len(Counter(nums[: i + 1])) - len(Counter(nums[i + 1 :]))
            res.append(ans)
        return res
