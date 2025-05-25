class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        wl = max(len(x), len(y))
        x = x.zfill(wl)
        y = y.zfill(wl)
        cnt = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                cnt += 1
        return cnt
