class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-float("inf")] * (k + 1) for _ in range(n)] for _ in range(m)]
        if grid[0][0] == 0:
            dp[0][0][0] = 0
        else:
            dp[0][0][1] = grid[0][0]
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if (i == 0 and j >= 1) or (j == 0 and i >= 1) or (i >= 1 and j >= 1):
                    if cur == 0:
                        for ii in range(k + 1):
                            dp[i][j][ii] = max(dp[i - 1][j][ii], dp[i][j - 1][ii])
                    else:
                        for ii in range(k - 1, -1, -1):
                            dp[i][j][ii + 1] = max(
                                dp[i][j][ii + 1],
                                dp[i - 1][j][ii] + cur,
                                dp[i][j - 1][ii] + cur,
                            )
        ans = max(dp[-1][-1])
        if ans == -float("inf"):
            return -1
        return ans
