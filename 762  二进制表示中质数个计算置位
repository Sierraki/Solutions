class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = 0
        for i in range(left, right + 1):
            a = bin(i)[2:]
            cur = 0
            for j in a:
                cur += int(j)
            s = True
            if cur == 1:
                s = False
            else:
                for k in range(2, cur):
                    if cur % k == 0:
                        s = False
            if s == True:
                cnt += 1
        return cnt
