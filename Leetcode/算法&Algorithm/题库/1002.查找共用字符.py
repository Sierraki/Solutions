class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for i in range(1, len(words)):
            cnt1 = Counter(words[i])
            for i, j in cnt.items():
                if i not in cnt1:
                    cnt[i] = 0
                else:
                    cnt[i] = min(j, cnt1[i])
        res = []
        for i, j in cnt.items():
            if j > 0:
                for _ in range(j):
                    res.append(i)
        return res
