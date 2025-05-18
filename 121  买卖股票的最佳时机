class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = prices[0]
        mal = 0
        lens = len(prices)
        for i in range(1, lens):
            if cur < prices[i] and prices[i] - cur > mal:
                mal = prices[i] - cur
            elif cur >= prices[i]:
                cur = prices[i]
        return mal
