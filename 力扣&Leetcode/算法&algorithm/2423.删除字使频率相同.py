class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        mx = max(cnt.values())
        mi = min(cnt.values())
        a = set([i for i, j in cnt.items() if j == mx])
        b = set([i for i, j in cnt.items() if j == mi])
        if len(cnt) == 1:
            return True
        elif len(b) == 1 and mi == 1 and len(a) + len(b) == len(set(word)):
            return True
        elif len(a) == 1 and mx - mi == 1:
            return True
        elif len(a) == 1 and mi == 0:
            return True
        elif mx == 1:
            return True
        return False
