class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lc1 = []
        lc2 = []
        for idx, i in enumerate(wordsDict):
            if i == word1:
                lc1.append(idx)
            if i == word2:
                lc2.append(idx)
        mi = float("inf")
        p1 = p2 = 0
        lc1.sort()
        lc2.sort()
        while p1 < len(lc1) and p2 < len(lc2):
            mi = min(abs(lc1[p1] - lc2[p2]), mi)
            if lc1[p1] >= lc2[p2]:
                p2 += 1
            else:
                p1 += 1
        return mi
