from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        # print(s)
        target = [i for i, j in cnt.items() if int(i) == j]
        # print(target)
        ans = ""
        for i in range(1, len(s)):
            if s[i] in target and s[i - 1] in target:
                if s[i] != s[i - 1]:
                    ans = [s[i - 1], s[i]]
                    break
        ans = "".join(ans)
        return ans
