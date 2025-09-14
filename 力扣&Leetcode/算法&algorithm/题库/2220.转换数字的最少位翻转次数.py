class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = bin(goal)[2:]
        b = bin(start)[2:]
        res = max(len(a), len(b))
        a = a.zfill(res)
        b = b.zfill(res)
        ans = 0
        for i in range(res):
            if a[i] != b[i]:
                ans += 1
        return ans
