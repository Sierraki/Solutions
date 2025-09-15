class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        cnt = dict(zip(order, [str(i) for i in range(1, 27)]))
        m = len(words)
        n = 0
        for i in words:
            n = max(n, len(i))
        res = [["00"] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j < len(words[i]):
                    res[i][j] = cnt[words[i][j]].zfill(2)
        for idx, i in enumerate(res):
            res[idx] = int("".join(i))
        return res == sorted(res)
