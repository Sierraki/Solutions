class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        for i in range(ord(s[0]), ord(s[3]) + 1):
            p1 = chr(i)
            for j in range(int(s[1]), int(s[4]) + 1):
                ans = p1 + str(j)
                res.append(ans)
        res.sort(key=lambda x: (x[0], x[1]))
        return res
