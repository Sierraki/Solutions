class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        mi = []
        for i in range(1, n + 1):
            if i == floor(sqrt(i)) ** 2:
                dp[i] = 1
                mi.append(i)
            else:
                for j in mi:
                    dif = i % (j)
                    if dp[i] == 0:
                        dp[i] = dp[j] * (i // (j)) + dp[i % (j)]
                    else:
                        dp[i] = min(dp[i], dp[j] * (i // (j)) + dp[i % (j)])
        return dp[-1]
