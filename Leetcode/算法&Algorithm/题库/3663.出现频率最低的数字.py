class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = Counter([int(i) for i in str(n)])
        ans = mi = float("inf")
        for i, j in cnt.items():
            if j == mi:
                mi = j
                ans = min(ans, i)
            elif j < mi:
                mi = j
                ans = i
        return ans
