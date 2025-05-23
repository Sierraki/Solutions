class Solution:
    def minChanges(self, n: int, k: int) -> int:
        cnt = 0
        n = bin(n)[2:]
        k = bin(k)[2:]
        l = max(len(n), len(k))
        n = n.zfill(l)
        k = k.zfill(l)
        print(l, n, k)
        for i in range(l):
            if n[i] != k[i]:
                if n[i] == "1":
                    cnt += 1
                else:
                    return -1
        return cnt
