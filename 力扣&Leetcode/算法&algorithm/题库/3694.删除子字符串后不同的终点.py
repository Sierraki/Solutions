class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        res1 = [0] * (n + 1)
        res2 = [0] * (n + 1)
        for i in range(n):
            if s[i] == "L":
                res1[i] = -1
            elif s[i] == "R":
                res1[i] = 1
            elif s[i] == "U":
                res2[i] = 1
            else:
                res2[i] = -1
        p1 = [0]
        p2 = [0]
        ss = 0
        for i in res1:
            ss += i
            p1.append(ss)
        ss = 0
        for i in res2:
            ss += i
            p2.append(ss)
        ans = set()
        for i in range(n):
            cur = s[i : i + k]
            if len(cur) == k:
                x = p1[-1] - (p1[i + k] - p1[i])
                y = p2[-1] - (p2[i + k] - p2[i])
                ans.add(f"{x}{'/'}{y}")
        return len(ans)
