class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0] = grid[0]
        for i in range(m - 1):
            for j in range(n):
                cur = grid[i][j]
                tar = moveCost[cur]
                for idx, k in enumerate(tar):
                    dp[i + 1][idx] = min(
                        dp[i + 1][idx], dp[i][j] + k + grid[i + 1][idx]
                    )
        return min(dp[-1])
