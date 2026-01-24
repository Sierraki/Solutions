class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        cur = []

        def check(s):
            if len(s) == 1:
                return True
            else:
                if 0 <= int(s) <= 255:
                    if s[0] != "0":
                        return True

        def backtracking(start):
            if len(cur) == 4:
                if start == n:
                    res.append(".".join(cur.copy()))
                return
            for i in range(start, n):
                if check(s[start : i + 1]):
                    cur.append(s[start : i + 1])
                    backtracking(i + 1)
                    cur.pop()

        backtracking(0)
        return res
