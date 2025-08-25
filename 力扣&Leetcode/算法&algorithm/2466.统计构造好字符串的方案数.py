class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * high
        if zero <= 1:
            dp[1] += 1
        if one <= 1:
            dp[1] += 1
        for i in range(2, len(dp)):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
        ans = 0
        for i in range(low, high + 1):
            ans += dp[i]
            ans %= mod
        return ans
