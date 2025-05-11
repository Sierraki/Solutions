class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        cur = 0
        for idx, i in enumerate(s):
            lc = t.index(i)
            # print(idx, lc)
            cur += abs(idx - lc)
        return cur
