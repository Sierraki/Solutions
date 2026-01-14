from math import floor, ceil
import sys

input = sys.stdin.readline


def fun(nums):
    mi = 0
    for i in nums:
        mi += floor(i)
    diff = 0 - mi
    ans = []
    for j in nums:
        if diff > 0 and not j.is_integer():
            ans.append(int(ceil(j)))
            diff -= 1
        else:
            ans.append(int(floor(j)))
    return ans


n = int(input())
nums = [float(input()) for _ in range(n)]
ans = fun(nums)
for i in ans:
    print((i))
