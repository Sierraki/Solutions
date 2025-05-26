from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.n = 0
        self.maxSize=maxSize

    def push(self, x: int) -> None:
        if self.n < self.maxSize:
            self.stack.append(x)
            self.n += 1

    def pop(self) -> int:
        if n > 0:
            stack.pop()
            n -= 1
