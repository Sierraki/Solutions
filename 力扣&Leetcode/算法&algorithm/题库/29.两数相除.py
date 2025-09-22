class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = dividend / divisor
        if res > 0:
            res = floor(res)
        else:
            res = ceil(res)
        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -(2**31):
            return res < -(2**31)
        return res
