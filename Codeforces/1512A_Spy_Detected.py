from collections import defaultdict
import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n = int(input())
    nums = input().split()
    for i in range(1, n - 1):
        if nums[i - 1] == nums[i + 1] and nums[i - 1] != nums[i]:
            print(i + 1)
            break
        elif nums[i] == nums[i + 1] and nums[i - 1] != nums[i]:
            print(i)
            break
        elif nums[i - 1] == nums[i] and nums[i+ 1] != nums[i]:
            print(i + 2)
            break
