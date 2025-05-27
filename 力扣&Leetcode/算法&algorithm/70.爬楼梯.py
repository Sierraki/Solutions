class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        c = 0
        i = 0
        while i < n:
            c = b + a
            a = b
            b = c
            i += 1
        return c
