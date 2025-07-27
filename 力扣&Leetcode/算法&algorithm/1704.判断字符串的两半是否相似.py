class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        p1 = s[:n]
        p2 = s[n:]
        cnt = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        a = b = 1
        for i in p1:
            if i.lower() in cnt:
                a += 1
        for i in p2:
            if i.lower() in cnt:
                b += 1
        return a == b
