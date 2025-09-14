class Solution:
    def maxProduct(self, n: int) -> int:
        res = [int(i) for i in str(n)]
        res.sort()
        return res[-1] * res[-2]
