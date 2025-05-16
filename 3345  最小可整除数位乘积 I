from itertools import count


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in count(n):
            cur = 1
            for j in str(i):
                cur *= int(j)
            if cur % t == 0:
                return i
