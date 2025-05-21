class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        cur = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i - 1] > prices[i]:
                left += 1
            else:
                if i == n - 1:
                    cur += prices[i] - prices[left]
                    left = i
                else:
                    if prices[i + 1] < prices[i]:
                        cur += prices[i] - prices[left]
                        left = i
        return cur
