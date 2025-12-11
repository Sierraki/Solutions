class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        dp = [[[-float("inf")] + [float("inf")] for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = dp[0][0][1] = grid[0][0]
        for i in range(1, n):
            dp[0][i][0] = dp[0][i][1] = dp[0][i - 1][0] * grid[0][i]
        for i in range(1, m):
            dp[i][0][0] = dp[i][0][1] = dp[i - 1][0][0] * grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                cur = grid[i][j]
                tar = [
                    dp[i - 1][j][0],
                    dp[i][j - 1][0],
                    dp[i - 1][j][1],
                    dp[i][j - 1][1],
                ]
                for k in tar:
                    dp[i][j][0] = max(dp[i][j][0], cur * k)
                    dp[i][j][1] = min(dp[i][j][1], cur * k)
        ans = max(dp[-1][-1])
        if ans < 0:
            return -1
        return ans % (10**9 + 7)
