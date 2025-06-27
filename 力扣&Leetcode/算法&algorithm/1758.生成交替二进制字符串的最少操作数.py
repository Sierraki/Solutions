class Solution:
    def minOperations(self, s: str) -> int:
        res1 = ["1" if i % 2 == 0 else "0" for i in range(len(s))]
        res2 = ["0" if i % 2 == 0 else "1" for i in range(len(s))]
        cnt1 = cnt2 = 0
        for i in range(len(s)):
            if s[i] != res1[i]:
                cnt1 += 1
            if s[i] != res2[i]:
                cnt2 += 1
        return min(cnt1, cnt2)


class Solution:
    def minOperations(self, s: str) -> int:
        cnt1 = cnt2 = 0
        for i in range(len(s)):
            if s[i] != str(i % 2 ^ 1):
                cnt1 += 1
            if s[i] != str(i % 2):
                cnt2 += 1
        return min(cnt1, cnt2)
