from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List
from fractions import Fraction


cont = [1, 5, 6, 6, 5, 7, 5, 5, 4, 7]


def fun(cont: list) -> list:
    res = 1 / cont[-1] + cont[-2]
    cont[-2] = res
    del cont[-1]
    return cont


while len(cont) > 1:
    cont = fun(cont)


ans = Fraction(cont[0])

print(ans)

an1 = [ans.numerator, ans.denominator]

print(an1)
