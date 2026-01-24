class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * (n)
        for i in range(1, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if i - 2 >= 0:
                if 0 < int(s[i - 2 : i]) <= 26 and s[i - 2] != "0":
                    dp[i] += dp[i - 2]
        return dp[-1]
