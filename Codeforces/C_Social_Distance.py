import sys
def fun(k, s):
    res = []
    cur = ""
    for i in s:
        if i == "0":
            cur += i
        else:
            res.append(cur)
            cur = ""
    res.append(cur)
    if len(res) == 1:
        return (len(res[0]) + k) // (1 + k)
    cnt = 0
    if len(res) >= 1:
        cnt += len(res[0]) // (k + 1)
    if len(res) >= 2:
        cnt += len(res[-1]) // (k + 1)
    if len(res) > 2:
        for i in res[1:-1]:
            cnt += max(0, (len(i) - k) // (1 + k))
    return cnt
input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n, k = list(map(int, input().split()))
    s = input().split()[0]
    print(fun(k, s))
