class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        dp[0][0] = [1, 1]
        for i in range(1, n):
            cur = grid[0][i]
            if cur == 0:
                dp[0][i] = [dp[0][i - 1][0], dp[0][i - 1][0]]
            else:
                dp[0][i] = [0, dp[0][i - 1][0]]
        for i in range(1, m):
            cur = grid[i][0]
            if cur == 0:
                dp[i][0] = [dp[i - 1][0][1], dp[i - 1][0][1]]
            else:
                dp[i][0] = [dp[i - 1][0][1], 0]
        for i in range(1, m):
            for j in range(1, n):
                cur = grid[i][j]
                if cur == 0:
                    res = dp[i - 1][j][1] + dp[i][j - 1][0]
                    dp[i][j] = [res, res]
                else:
                    dp[i][j][0] = dp[i - 1][j][1]
                    dp[i][j][1] = dp[i][j - 1][0]
        return (dp[-1][-1][-1]) % mod
