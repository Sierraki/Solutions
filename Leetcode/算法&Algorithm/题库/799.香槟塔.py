class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (100) for _ in range(100)]
        if poured >= 1:
            dp[0][0] = 1
            poured -= 1
            dp[1][0] = dp[1][1] = poured / 2
        else:
            dp[0][0] = poured
        for i in range(1, len(dp)):
            for j in range(i + 1):
                if dp[i][j] >= 1:
                    res = dp[i][j] - 1
                    if i + 1 < len(dp) and j + 1 < len(dp[0]):
                        dp[i + 1][j] += res / 2
                        dp[i + 1][j + 1] += res / 2
        if dp[query_row][query_glass] >= 1:
            return 1
        return dp[query_row][query_glass]
