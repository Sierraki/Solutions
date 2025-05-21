class Solution:
    def reverseDegree(self, s: str) -> int:
        cur = 0
        for idx, i in enumerate(s, start=1):
            cur += (123 - ord(i)) * idx
        return cur
