class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        if k >= max(n - 1, m - 1):
            return 1
        nl = 2 * k + 1
        rows = ceil(n / nl)
        cols = ceil(m / nl)
        return rows * cols