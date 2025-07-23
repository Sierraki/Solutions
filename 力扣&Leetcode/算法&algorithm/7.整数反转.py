class Solution:
    def reverse(self, x: int) -> int:
        swap = True
        if x < 0:
            swap = False
        num = str(abs(x))[::-1]
        if not swap:
            res = -1 * int(num)
        else:
            res = int(num)
        if not (-(2**31) <= res <= 2**31 - 1):
            return 0
        return res
