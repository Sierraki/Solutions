class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        cnt = set(word1 + word2)
        for i in cnt:
            if abs(cnt1[i] - cnt2[i]) > 3:
                return False
        return True
