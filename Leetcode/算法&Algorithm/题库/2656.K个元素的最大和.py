class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + (1 + (k - 1)) * (k - 1) // 2
