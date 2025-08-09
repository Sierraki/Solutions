from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List
from fractions import Fraction


class TripleInOne:

    def __init__(self, stackSize: int):
        self.nums = deque([])
        self.n = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.nums) < self.n:
            self.nums.insert(stackNum, value)
        return self.nums

    def pop(self, stackNum: int) -> int:
        if not self.nums:
            return -1
        del self.nums[stackNum]

    def peek(self, stackNum: int) -> int:
        if not self.nums:
            return -1
        return self.nums[stackNum]

    def isEmpty(self, stackNum: int) -> bool:
        
