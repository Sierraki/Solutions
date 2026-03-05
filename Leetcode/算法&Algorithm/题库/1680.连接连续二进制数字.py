class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = "0"
        for i in range(1, n + 1):
            ans += bin(i)[2:]
        return int(ans, 2) % (10**9 + 7)
