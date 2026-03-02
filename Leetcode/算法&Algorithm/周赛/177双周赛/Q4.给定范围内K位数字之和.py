class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        mod = 10**9 + 7
        n = r - l + 1
        total = (l + r) * n // 2
        total %= mod
        # 每位贡献
        gx_bit = pow(n, k - 1, mod)
        res = total * gx_bit
        res1 = pow(9, mod - 2, mod)
        total1 = pow(10, k, mod) - 1 + mod
        ans = total1 * res1
        return (res * ans) % mod
