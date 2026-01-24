import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
res = [[j, i] for i, j in enumerate(nums)]
res.sort()
print(" ".join(map(str, [i[1] + 1 for i in res][:3])))
