class Solution:
    def concatHex36(self, n: int) -> str:
        p1 = hex(n**2)[2:]

        def fun(n):
            if n == 0:
                return "0"
            digits = "0123456789abcdefghijklmnopqrstuvwxyz"
            res = ""
            while n > 0:
                res = digits[n % 36] + res
                n //= 36
            return res

        res = p1 + fun(n**3)
        return "".join(map(str.upper, res))
