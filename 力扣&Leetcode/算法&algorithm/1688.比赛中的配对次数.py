class Solution:
    def numberOfMatches(self, n: int) -> int:
        def fun(n: int):
            if n % 2 == 0:
                return [n // 2, n // 2]
            else:
                return [(n - 1) / 2, (n - 1) / 2 + 1]

        # 配对次数  剩下多少人
        a = 0
        b = float("inf")
        while b > 1:
            ans = fun(n)
            a += ans[0]
            b = ans[1]
            n = int(b)
        return int(a)
