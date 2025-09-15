class Solution:
    def divide(self, a: int, b: int) -> int:
        swap = False
        if (b < 0 and a > 0) or (b > 0 and a < 0):
            swap = True
        ans = abs(a) // abs(b)
        if swap:
            ans = -ans
        if not (-(2**31) <= ans <= 2**31 - 1):
            return 2**31 - 1
        return ans
