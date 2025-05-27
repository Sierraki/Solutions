class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        left = 0
        a = []
        for idx, i in enumerate(s):
            if idx == len(s) - 1:
                if s[idx - 1] != i:
                    a.append(1)
                else:
                    a.append(idx - left + 1)
            elif i == s[left] and s[idx + 1] != i:
                a.append(idx - left + 1)
                left = idx + 1
        cnt = 0
        for i in range(1, len(a)):
            cnt += min(a[i], a[i - 1])
        return cnt
