class Solution:
    def fib(self, n: int) -> int:
        res = 0
        if n < 2:
            return n
        a, b, res = 0, 1, 0
        for i in range(n - 1):
            res = b + a
            a = b
            b = res
        return res
