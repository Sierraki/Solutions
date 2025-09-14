class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(2, n + 1):
            tar = i // 2
            dp[i] = max(
                max(tar, dp[tar]) * max(i - tar, dp[i - tar]),
                max(tar + 1, dp[tar + 1]) * max(i - tar - 1, dp[i - tar - 1]),
                max(tar - 1, dp[tar - 1]) * max(i - tar + 1, dp[i - tar + 1]),
            )
        return dp[-1]
