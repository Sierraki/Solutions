class Solution:
    def minimumFlips(self, n: int) -> int:
        res1 = bin(n)[2:]
        res2 = res1[::-1]
        cnt = 0
        for i in range(len(res1)):
            if res1[i] != res2[i]:
                cnt += 1
        return cnt
