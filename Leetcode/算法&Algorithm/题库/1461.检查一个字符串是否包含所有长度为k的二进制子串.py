class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ans = 2**k
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i : i + k])
        return len(seen) == ans
