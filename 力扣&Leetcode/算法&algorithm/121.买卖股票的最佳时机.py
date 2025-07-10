class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = float("inf")
        mx = 0
        for i in prices:
            if i < mi:
                mi = i
            else:
                mx = max(mx, i - mi)
        return mx
