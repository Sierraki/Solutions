class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        last = [-prices[0], 0] * k
        cur = [0, 0] * k
        for i in range(1, n):
            for j in range(len(cur)):
                if j == 0:
                    cur[0] = max(last[0], 0 - prices[i])
                else:
                    if j % 2 == 1:
                        cur[j] = max(last[j], last[j - 1] + prices[i])
                    else:
                        cur[j] = max(last[j], last[j - 1] - prices[i])
            last = cur
        return cur[-1]
