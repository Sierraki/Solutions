import sys
from collections import deque

input = sys.stdin.readline


def cut(n, t):
    a = n // 2
    b = (n + 1) // 2
    if a not in used:
        res.append([a, t + 1])
        used.add(a)
    if b not in used and b != a:
        res.append([b, t + 1])
        used.add(b)


def fun(n, tar):
    if n == tar:
        return 0
    if n < tar:
        return -1
    res.clear()
    used.clear()
    res.append([n, 0])
    used.add(n)
    while res:
        cur_val, cur_time = res.popleft()
        if cur_val == tar:
            return cur_time
        if cur_val < tar:
            continue
        cut(cur_val, cur_time)
    return -1


size = int(input())
for _ in range(size):
    nums = iter(input().split())
    n, tar = int(next(nums)), int(next(nums))
    res = deque([])
    used = set()
    print(fun(n, tar))
