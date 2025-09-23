class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)):
            if i <= mx:
                mx = max(mx, nums[i] + i)
        return mx >= len(nums) - 1
