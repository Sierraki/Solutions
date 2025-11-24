class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.cnt = defaultdict(list)
        for i, j in enumerate(wordsDict):
            self.cnt[j].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        p1 = p2 = 0
        mi = float("inf")
        while p1 < len(self.cnt[word1]) and p2 < len(self.cnt[word2]):
            mi = min(abs(self.cnt[word1][p1] - self.cnt[word2][p2]), mi)
            if mi == 1:
                break
            if self.cnt[word1][p1] > self.cnt[word2][p2]:
                p2 += 1
            else:
                p1 += 1
        return mi


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
