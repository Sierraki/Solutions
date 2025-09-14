class Solution:
    def leastMinutes(self, n: int) -> int:
        if n <= 2:
            return n
        tar = 1
        ans = 1
        while ans < n:
            tar += 1
            ans = 2**tar
        return tar + 1
