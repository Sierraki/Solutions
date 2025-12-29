class Solution:
    def removeZeros(self, n: int) -> int:
        res = str(n).split("0")
        return int("".join(res))
