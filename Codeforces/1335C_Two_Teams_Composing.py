from collections import Counter
import sys


def fun(nums):
    cnt = Counter(nums)
    a = max(cnt.values())
    b = len(cnt) - 1
    return max(min(a - 1, b + 1), min(a, b))


data = iter(sys.stdin.read().split())
size = int(next(data))
for _ in range(size):
    n = int(next(data))
    nums = [int(next(data)) for _ in range(n)]
    print(fun(nums))
