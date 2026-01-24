class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for i in words:
            if len(i) >= len(pref):
                if i[: len(pref)] == pref:
                    ans += 1
        return ans
