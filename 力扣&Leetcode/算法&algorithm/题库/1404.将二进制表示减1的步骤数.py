class Solution:
    def numSteps(self, s: str) -> int:
        tar = int(s, 2)
        cnt = 0
        while tar > 1:
            if tar % 2 == 1:
                tar += 1
            else:
                tar //= 2
            cnt += 1
        return cnt
