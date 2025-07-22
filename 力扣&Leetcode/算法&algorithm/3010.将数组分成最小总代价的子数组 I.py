class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        del nums[0]
        mi = float("inf")
        for idx, i in enumerate(nums):
            if i < mi:
                lc = idx
                mi = i
        ans += mi
        del nums[lc]
        mi = float("inf")
        for idx, i in enumerate(nums):
            if i < mi:
                lc = idx
                mi = i
        ans += mi
        return ans
