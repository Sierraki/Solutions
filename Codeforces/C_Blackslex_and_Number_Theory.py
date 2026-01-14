import sys

input = lambda: sys.stdin.readline()


def fun(nums):
    nums.sort()
    # print(nums)
    mi1 = nums[0]
    mi2 = nums[1]
    return max(mi1, mi2 - mi1)


size = int(input())

for _ in range(size):
    n = int(input())
    nums = list(map(int, input().split()))
    print(fun(nums))
