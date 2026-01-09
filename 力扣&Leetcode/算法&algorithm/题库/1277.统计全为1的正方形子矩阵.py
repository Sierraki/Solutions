class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        dp = [[0] * n for _ in range(m)]
        dp[0] = matrix[0]
        for i in range(m):
            dp[i][0] = matrix[i][0]
            ans += matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans += dp[i][j]
        if matrix[0][0] == 1:
            ans -= 1
        return ans + sum(matrix[0])
