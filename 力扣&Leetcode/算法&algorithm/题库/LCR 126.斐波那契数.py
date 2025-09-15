class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        mod = 10**9 + 7
        if n == 1:
            return 1
        if n == 0:
            return 0

        while n >= 2:
            ans = a + b
            a = b
            b = ans
            n -= 1
        return b % mod
