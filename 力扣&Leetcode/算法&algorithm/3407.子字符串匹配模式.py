class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        l, r = p.split("*")
        return any(
            s[j : j + len(l)] == l and r in s[j + len(l) :] for j in range(len(s))
        )
