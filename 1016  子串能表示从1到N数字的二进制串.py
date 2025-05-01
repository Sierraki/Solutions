class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(bin(i)[2:] in s for i in range(1, n + 1))