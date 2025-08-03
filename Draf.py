from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


date1 = "2019-06-29"
date2 = "2019-06-30"
monp = {
    1: 0,
    2: 31,
    3: 59,
    4: 90,
    5: 120,
    6: 151,
    7: 181,
    8: 212,
    9: 243,
    10: 273,
    11: 304,
    12: 334,
}
monr = {
    1: 0,
    2: 31,
    3: 60,
    4: 91,
    5: 121,
    6: 152,
    7: 182,
    8: 213,
    9: 244,
    10: 274,
    11: 305,
    12: 335,
}


def fun(s: str) -> int:
    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[8:])

    swap = False
    if y % 4 == 0 and y % 100 != 0 or (y % 400 == 0):
        swap = True

    res = 0
    if y <= 1972:
        if y == 1971:
            res = 0
            res += monr[m] + d
        else:
            res = 365
            res += monp[m] + d
    else:
        dif = y - 1972
        res = dif * 365 + 365 + 366 + dif // 4
        if swap:
            res -= 366
            res += monr[m] + d
        else:
            res -= 365
            res += monp[m] + d
    return res


print(abs(fun(date1) - fun(date2)))


print(fun("2100-09-22"))

print(fun("1991-03-12"))
