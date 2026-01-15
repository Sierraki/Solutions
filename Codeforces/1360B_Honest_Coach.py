import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    ans = float("inf")
    for i in range(1, n):
        ans = min(ans, nums[i] - nums[i - 1])
    print(ans)
