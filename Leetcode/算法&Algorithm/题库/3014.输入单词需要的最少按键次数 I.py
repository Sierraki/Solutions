class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        a = n // 8
        b = n % 8
        res = 0
        if a == 0:
            res = b
        else:
            res = (1 + a) * a * 4 + b * (a + 1)
        return res
