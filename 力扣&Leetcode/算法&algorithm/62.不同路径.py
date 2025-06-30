class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m * n < 2:
            return 1
        dp = [0] * m * n
        for i in range(1, m * n):
            if i < n:
                dp[i] = 1
            elif i > 0 and i % n == 0:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - n]
        return dp[-1]
