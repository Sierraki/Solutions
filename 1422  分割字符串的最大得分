class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        a = []
        for i in range(1, n):
            cnt0 = s[0:i].count("0")
            cnt1 = s[i:n].count("1")
            a.append(cnt0 + cnt1)
        a.sort(reverse=True)
        return a[0]
