import sys

input = sys.stdin.readline
n, k, x = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
cnt = n - k
if sum(nums) - sum(nums[: (n - k)]) >= x:
    pin = n - k
    while x > 0:
        x -= nums[pin]
        pin += 1
        cnt += 1
    print(cnt)
else:
    print(-1)
