class Solution:
    def hammingWeight(self, n: int) -> int:
        a = str(bin(n))
        a = a[2:]
        b = 0
        for i in a:
            b = b + int(i)
        return b
