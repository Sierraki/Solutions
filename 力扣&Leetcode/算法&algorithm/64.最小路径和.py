class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        nums = [j for i in grid for j in i]
        dp = [0] * m * n
        s = 0
        for i in range((m * n)):
            if i < n:
                s += nums[i]
                dp[i] = s
            elif i > 0 and i % n == 0:
                dp[i] = nums[i] + dp[i - n]
            else:
                dp[i] = min(dp[i - n], dp[i - 1]) + nums[i]
        return dp[-1]
