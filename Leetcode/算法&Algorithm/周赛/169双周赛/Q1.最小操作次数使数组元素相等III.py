class Solution:
    def minMoves(self, nums: List[int]) -> int:
        tar = max(nums)
        ans = 0
        for i in nums:
            ans += tar - i
        return ans
