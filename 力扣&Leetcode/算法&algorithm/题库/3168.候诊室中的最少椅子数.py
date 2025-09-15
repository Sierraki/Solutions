class Solution:
    def minimumChairs(self, s: str) -> int:
        cnt = 0
        mi = float("inf")
        for i in s:
            if i == "E":
                cnt -= 1
            else:
                cnt += 1
            mi = min(mi, cnt)
        return abs(mi)
