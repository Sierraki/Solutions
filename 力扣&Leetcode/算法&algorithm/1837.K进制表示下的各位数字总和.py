class Solution:
    def sumBase(self, n: int, k: int) -> int:
        s = 0
        while n > 0:
            ans = n % k
            n = n // k
            s += ans
        return s


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        s = 0
        while n > 0:
            n, ans = divmod(n, k)
            s += ans
        return s
