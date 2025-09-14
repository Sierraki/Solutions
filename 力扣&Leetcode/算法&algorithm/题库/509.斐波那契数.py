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


class Solution:

    def fib(self, n: int) -> int:
        def a(n):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            else:
                return a(n - 1) + a(n - 2)
        return a(n)
