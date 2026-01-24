class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        last = [-prices[0], 0, -prices[0], 0]
        cur = [0, 0, 0, 0]
        for i in range(1, n):
            cur[0] = max(last[0], 0 - prices[i])
            cur[1] = max(last[1], last[0] + prices[i])
            cur[2] = max(last[2], last[1] - prices[i])
            cur[3] = max(last[3], last[2] + prices[i])
            last = cur
        return cur[-1]
