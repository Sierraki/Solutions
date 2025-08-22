class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0):
            if month == 2:
                return 29
        else:
            if month == 2:
                return 28
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30
