class Solution:
    def addDigits(self, num: int) -> int:
        s = num
        while s >= 10:
            s = 0
            for i in str(num):
                s = int(s) + int(i)
            num = s
        return s
