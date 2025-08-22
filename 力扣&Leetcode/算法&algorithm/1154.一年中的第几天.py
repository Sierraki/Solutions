class Solution:
    def dayOfYear(self, date: str) -> int:
        y = int(date[:4])
        m = int(date[5:7])
        d = int(date[8:])
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            a = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ans = sum(a[: m - 1]) + d
        return ans
