class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        c = 0
        i = 0
        while i < n:
            c = b + a
            a = b
            b = c
            i += 1
        return c


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 1  # dp[i-2], dp[i-1]
        for _ in range(2, n + 1):
            a, b = b, a + b  # 更新为新的 dp[i]
        return b