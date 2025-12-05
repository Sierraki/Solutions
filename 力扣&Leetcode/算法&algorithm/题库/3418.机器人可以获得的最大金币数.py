class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[-float("inf") for _ in range(3)] for _ in range(n)] for _ in range(m)]
        # k使用的次数
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0
        for i in range(m):
            for j in range(n):
                cur = coins[i][j]
                if (
                    (i == 0 and j - 1 >= 0)
                    or (j == 0 and i - 1 >= 0)
                    or (i >= 1 and j >= 1)
                ):
                    for k in [0, 1, 2]:
                        res = max(dp[i - 1][j][k], dp[i][j - 1][k])
                        dp[i][j][k] = max(dp[i][j][k], res + cur)
                        if cur < 0:
                            if k + 1 <= 2:
                                dp[i][j][k + 1] = max(dp[i][j][k + 1], res)
        return max(dp[-1][-1])
