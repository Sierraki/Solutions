class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def fun(res1=str):
            res = []
            for i in res1:
                if i != "#":
                    res.append(i)
                else:
                    if res:
                        res.pop()
            return res

        return fun(s) == fun(t)
