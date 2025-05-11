from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        a = []
        for i in range(lowLimit, highLimit + 1):
            print(str(i))
            cur = 0
            for j in str(i):
                cur += int(j)
            a.append(cur)
        cnt = Counter(a)
        return max(cnt.values())
