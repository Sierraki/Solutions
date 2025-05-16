class Solution:
    def trainWays(self, num: int) -> int:
        a, b = 1, 1
        for _ in range(num):
            a, b = b, (a + b) % 1000000007
        return a
