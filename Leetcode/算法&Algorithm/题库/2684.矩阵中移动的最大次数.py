class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        def check(i, j):
            res = 0
            for k in [-1, 0, 1]:
                if j == 1:
                    if 0 <= i + k < m and grid[i + k][j - 1] < grid[i][j]:
                        res = max(res, dp[i + k][j - 1] + 1)
                elif j > 1:
                    if (
                        0 <= i + k < m
                        and grid[i + k][j - 1] < grid[i][j]
                        and dp[i + k][j - 1] > 0
                    ):
                        res = max(res, dp[i + k][j - 1] + 1)
            return res

        ans = 0
        for i in range(1, n):
            for j in range(m):
                dp[j][i] = check(j, i)
                ans = max(ans, dp[j][i])
        return ans
