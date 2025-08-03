class Solution:
    def waysToStep(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % (10**9 + 7)
        return dp[-1]
