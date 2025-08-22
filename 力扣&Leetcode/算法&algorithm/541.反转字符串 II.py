class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k >= len(s):
            return s[::-1]
        s = [i for i in s]
        for i in range(0, len(s), 2 * k):
            s[i : i + k] = reversed(s[i : i + k])
        return "".join(s)
