class Solution:
    def maxSales(self, sales: List[int]) -> int:
        prefix = []
        mi = []
        a = float("inf")
        s = 0
        for i in sales:
            s += i
            prefix.append(s)
            a = min(a, s)
            mi.append(a)
        ans = prefix[0]
        for i in range(1, len(mi)):
            ans = max(prefix[i] - mi[i - 1], ans, prefix[i])
        return ans


class Solution:
    def maxSales(self, sales: List[int]) -> int:
        ans = sales[0]
        cur = 0
        for x in sales:
            cur = max(cur + x, x)
            ans = max(ans, cur)
        return ans
