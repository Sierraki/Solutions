class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = max(nums[1], nums[0])
        for i in range(3, len(nums) + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
        return dp[-1]
