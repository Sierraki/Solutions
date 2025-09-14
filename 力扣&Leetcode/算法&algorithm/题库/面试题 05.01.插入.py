class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        res = bin(N)[2:]
        tar = bin(M)[2:]
        res = res.zfill(len(tar))
        p1 = res[: -j - 1]
        p2 = res[-j - 1 : -i]
        if i == 0:
            p3 = ""
        else:
            p3 = res[-i:]
        if len(tar) >= j - i + 1:
            p2 = tar[-(j - i + 1) :]
        else:
            p2 = "0" * (j - i + 1 - len(tar)) + tar
        ans = p1 + p2 + p3
        return int(ans, 2)
