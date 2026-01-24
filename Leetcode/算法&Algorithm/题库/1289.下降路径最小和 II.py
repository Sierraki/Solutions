class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = grid[i][j]
                else:
                    for k in range(n):
                        if k != j:
                            dp[i][j] = min(dp[i - 1][k] + grid[i][j], dp[i][j])
        return min(dp[-1])
