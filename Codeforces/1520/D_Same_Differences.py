from collections import Counter
import sys

input = sys.stdin.readline


def fun(nums):
    ans = 0
    cnt = Counter()
    for i, j in enumerate(nums):
        cnt[j - i] += 1
    for i in cnt.values():
        if i >= 2:
            ans += i * (i - 1) // 2
    return ans


n = int(input())
for _ in range(n):
    m = input()
    nums = list(map(int, input().split()))
    print(fun(nums))
