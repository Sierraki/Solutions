class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        l = max(m, n)
        return max(l * k - k * k, 0)
