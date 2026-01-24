class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return "a" * 1 + "b" * (n - 1)
        else:
            if n > 1:
                return "a" + "b" + "c" * (n - 2)
            else:
                return "a"
