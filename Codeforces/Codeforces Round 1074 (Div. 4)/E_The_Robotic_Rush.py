import sys
from bisect import bisect_left

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n, m, k = map(int, input().split())
    rb = list(map(int, input().split()))
    mo = list(map(int, input().split()))
    s = input()[:-1]
    rb.sort()
    mo.sort()
    curL = [0] * (k + 1)
    curR = [0] * (k + 1)
    diff = 0
    left, right = 0, 0
    for i in range(1, k + 1):
        if s[i - 1] == "L":
            diff -= 1
        else:
            diff += 1
        left = max(left, -diff)
        right = max(right, diff)
        curL[i] = left
        curR[i] = right
    die = []
    for p in rb:
        idx = bisect_left(mo, p)
        dist_L = p - mo[idx - 1] if idx > 0 else float("inf")
        dist_R = mo[idx] - p if idx < m else float("inf")
        t_L = bisect_left(curL, dist_L)
        t_R = bisect_left(curR, dist_R)
        die_cnt = min(t_L, t_R)
        if die_cnt <= k:
            die.append(die_cnt)
    die.sort()
    die_idx = 0
    res = []
    for i in range(1, k + 1):
        while die_idx < len(die) and die[die_idx] <= i:
            die_idx += 1
        res.append(n - die_idx)
    print(*res)
