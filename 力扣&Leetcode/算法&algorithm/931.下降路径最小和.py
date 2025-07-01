class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if i == 0:
                dp[0] = matrix[0]
            else:
                for j in range(n):
                    if j == 0:
                        dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
                    elif j == n - 1:
                        dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
                    else:
                        dp[i][j] = matrix[i][j] + min(
                            dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]
                        )
        return min(dp[-1])
