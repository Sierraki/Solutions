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


class Solution:
    def waysToStep(self, n: int) -> int:
        a = 1
        b = 2
        c = 4
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            for i in range(n - 3):
                ans = (a + b + c) % 1000000007
                a = b
                b = c
                c = ans
            return c
