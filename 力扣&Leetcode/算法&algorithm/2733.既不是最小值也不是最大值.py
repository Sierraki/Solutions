class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        res = sorted(list(set(nums)))
        ans = -1
        if len(res) > 2:
            ans = res[1]
        return ans
