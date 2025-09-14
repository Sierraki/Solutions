class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = [i for i in num]
        while num[-1] == "0":
            num.pop()
        return "".join(num)
