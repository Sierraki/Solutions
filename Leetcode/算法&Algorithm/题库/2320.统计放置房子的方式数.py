class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7
        dp0 = [0] * (n + 1)
        dp1 = [0] * (n + 1)
        dp0[1] = dp1[1] = 1
        for i in range(2, n + 1):
            dp0[i] = dp0[i - 1] + dp1[i - 1]
            dp1[i] = dp0[i - 1]
        res = dp0[-1] + dp1[-1]
        return (res**2) % mod
