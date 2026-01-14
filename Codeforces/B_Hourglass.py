import sys

input = sys.stdin.readline


def fun(s, k, m):
    rem = m % (2 * k)
    if rem < k:
        res = s - rem
        if res < 0:
            res = 0
    else:
        cur = min(s, k)
        res = cur - (rem - k)
        if res < 0:
            res = 0
    return res


size = int(input())
for _ in range(size):
    nums = list(map(int, input().split()))
    print(fun(nums[0], nums[1], nums[2]))
