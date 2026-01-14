import sys

input = sys.stdin.readline

size = int(input())
for _ in range(size):
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    print(a * b + 1)
