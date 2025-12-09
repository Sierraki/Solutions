class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(1, n + 1):
            if i == 1:
                dp[0][i] = -prices[i - 1]
                dp[1][i] = 0
            else:
                dp[0][i] = max(dp[0][i - 1], dp[1][i - 2] - prices[i - 1])
                dp[1][i] = max(dp[0][i - 1] + prices[i - 1], dp[1][i - 1])
        return dp[-1][-1]
