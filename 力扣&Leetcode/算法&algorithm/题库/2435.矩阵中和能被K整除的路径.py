class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(1, n):
            cur = grid[0][i]
            for jdx, j in enumerate(dp[0][i - 1]):
                if j != 0:
                    dp[0][i][(jdx + cur) % k] += j
        for i in range(1, m):
            cur = grid[i][0]
            for jdx, j in enumerate(dp[i - 1][0]):
                if j != 0:
                    dp[i][0][(jdx + cur) % k] += j
        for i in range(1, m):
            for j in range(1, n):
                cur = grid[i][j]
                tar = [0] * k
                for idx in range(k):
                    tar[idx] = dp[i - 1][j][idx] + dp[i][j - 1][idx]
                for k1, k2 in enumerate(tar):
                    dp[i][j][(k1 + cur) % k] += k2
        return dp[-1][-1][0] % mod
