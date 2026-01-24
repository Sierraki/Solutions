class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = []
        n = len(prices)
        pin = 0
        cur = -1
        left = n
        for i in range(1, n):
            if prices[i] - prices[i - 1] == -1:
                cur = i
            else:
                if pin < cur:
                    res.append(cur - pin + 1)
                    left -= cur - pin + 1
                pin = i
        if pin < cur:
            res.append(cur - pin + 1)
            left -= cur - pin + 1
        ans = 0
        for i in res:
            ans += (1 + i) * i // 2
        return ans + left
