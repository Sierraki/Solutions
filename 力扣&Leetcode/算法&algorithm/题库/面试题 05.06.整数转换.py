class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        res1 = bin(A & 0xFFFFFFFF)[2:]
        res2 = bin(B & 0xFFFFFFFF)[2:]
        n = max(len(res1), len(res2))
        ans1 = res1.zfill(n)
        ans2 = res2.zfill(n)
        ans = 0
        for i in range(n):
            if ans1[i] != ans2[i]:
                ans += 1
        return ans
