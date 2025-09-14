class Solution:
    def smallestNumber(self, n: int) -> int:
        def fun(n: int) -> bool:
            res = Counter(bin(n)[2:])
            return res["0"] == 0

        while n != 0:
            if not fun(n):
                n += 1
            else:
                return n
