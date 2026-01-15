import sys


def fun(n, w, nums):
    bkt = [[] for _ in range(2 * w)]
    for i in range(n):
        bkt[i % (2 * w)].append(i)
    res = []
    for i in bkt:
        cur = 0
        for j in i:
            cur += nums[j]
        res.append(cur)
    ans = cur = sum(res[:w])
    res += res
    for i in range(w, len(res)):
        cur += res[i] - res[i - w]
        ans = min(ans, cur)
    return ans


input = sys.stdin.readline
size = int(input())
for _ in range(size):
    a, b = map(int, input().split())
    nums = list(map(int, input().split()))
    print(fun(a, b, nums))
