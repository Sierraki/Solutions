class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        cnt = defaultdict(list)
        for i, j in enumerate(wordsDict):
            cnt[j].append(i)
        p1 = p2 = 0
        mi = float("inf")
        if word1 != word2:
            while p1 < len(cnt[word1]) and p2 < len(cnt[word2]):
                mi = min(mi, abs(cnt[word1][p1] - cnt[word2][p2]))
                if mi == 1:
                    break
                if cnt[word1][p1] > cnt[word2][p2]:
                    p2 += 1
                else:
                    p1 += 1
        else:
            for i in range(1, len(cnt[word1])):
                mi = min(mi, cnt[word1][i] - cnt[word1][i - 1])
        return mi
