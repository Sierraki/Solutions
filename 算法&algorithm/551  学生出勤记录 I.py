class Solution:
    def checkRecord(self, s: str) -> bool:
        a_cnt = 0
        stat = True
        n = len(s)
        # print(n)
        for i in range(n):
            if s[i] == "A":
                a_cnt += 1
            elif i + 2 <= n - 1 and s[i] == s[i + 1] == s[i + 2] == "L":
                stat = False
            else:
                continue
        if a_cnt >= 2:
            stat = False
        return stat
