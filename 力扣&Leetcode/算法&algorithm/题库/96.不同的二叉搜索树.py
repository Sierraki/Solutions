class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = dp[0] = 1
        for i in range(2, n + 1):
            for l in range(0, n):
                dp[i] += dp[l] * dp[i - l - 1]
        return dp[-1]
