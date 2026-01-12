from collections import Counter
import sys


def fun(nums):
    if m % 2 == 0:
        odd = Counter()
        even = Counter()
        odd_cnt = 0
        even_cnt = 0
        for i in nums:
            if i % 2 == 0:
                even[i] += 1
                even_cnt += 1
            else:
                odd[i] += 1
                odd_cnt += 1
        for i in even.keys():
            if i + 1 in odd or i - 1 in odd:
                return "YES"
        if odd_cnt % 2 == 0 and even_cnt % 2 == 0:
            return "YES"
    return "NO"


data = iter(sys.stdin.read().split())
n = int(next(data))
for _ in range(n):
    m = int(next(data))
    nums = [int(next(data)) for _ in range(m)]
    print(fun(nums))
