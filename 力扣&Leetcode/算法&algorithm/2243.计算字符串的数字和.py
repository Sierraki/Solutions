class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def fun1(x: int):
            c = 0
            for i in str(x):
                c += int(i)
            return c

        def fun2(s: str, k: int) -> str:
            res = []
            for i in range(0, len(s), k):
                res.append(fun1(s[i : i + k]))
            return "".join(map(str, res))

        while len(s) > k:
            s = fun2(s, k)
        return s
