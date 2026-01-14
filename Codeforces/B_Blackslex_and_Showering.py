import sys


def fun(nums):
    total = 0
    for i in range(1, n):
        total += abs(nums[i] - nums[i - 1])
    mi = float("inf")
    for i in range(1, n - 1):
        tar = (
            total
            - abs(nums[i] - nums[i - 1])
            - abs(nums[i + 1] - nums[i])
            + abs(nums[i + 1] - nums[i - 1])
        )
        mi = min(mi, tar)
    if n >= 2:
        mi = min(mi, total - abs(nums[0] - nums[1]), total - abs(nums[-1] - nums[-2]))
    return mi


input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n = int(input())
    nums = list(map(int, input().split()))
    print(fun(nums))
