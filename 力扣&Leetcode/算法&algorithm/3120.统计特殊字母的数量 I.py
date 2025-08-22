class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = defaultdict(set)
        for i in word:
            cnt[i.lower()].add(i)
        c = 0
        for i in cnt.values():
            if len(i) >= 2:
                c += 1
        return c
