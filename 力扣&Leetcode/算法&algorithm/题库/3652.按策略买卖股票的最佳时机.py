class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        pf = []
        pf1 = []
        s = 0
        s1 = 0
        for i in range(n):
            s += prices[i] * strategy[i]
            pf.append(s)
            s1 += prices[i]
            pf1.append(s1)
        ans = max(pf[-1], pf[-1] + pf1[k - 1] - pf1[k // 2 - 1] - pf[k - 1])
        for i in range(k, n):
            ans = max(ans, pf[-1] + pf1[i] - pf1[i - k // 2] - (pf[i] - pf[i - k]))
        return ans
