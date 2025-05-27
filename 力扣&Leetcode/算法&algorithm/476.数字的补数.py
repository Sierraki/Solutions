class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        a = []
        for i in num:
            if i == "1":
                a.append("0")
            else:
                a.append("1")
        return int("".join(a), 2)
