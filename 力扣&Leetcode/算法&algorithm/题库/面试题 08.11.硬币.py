class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(4)]
        coins = [1, 5, 10, 25]
        mod = 10**9 + 7
        for i in range(1, n + 1):
            dp[0][i] = 1
        for i in range(1, 4):
            for j in range(1, n + 1):
                # j代表现在是多少钱
                # coins【i】代表当前硬币
                if coins[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 要不要当前
                    # 要
                    if dp[i][j - coins[i]] == 0:
                        dp[i][j] += 1
                    else:
                        dp[i][j] += dp[i][j - coins[i]]
                    # 不要
                    dp[i][j] += dp[i - 1][j]
                dp[i][j] = dp[i][j] % mod
        return dp[-1][-1]
