class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [i for i, j in Counter((s1 + " " + s2).split()).items() if j == 1]
