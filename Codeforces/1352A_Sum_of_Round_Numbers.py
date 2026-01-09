import sys


def fun(num):
    res = []
    num = str(num)
    cnt = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != "0":
            res.append(int(num[i]) * (10**cnt))
        cnt += 1
    return res


n = int(input())
for _ in range(n):
    num = int(input())
    ans = sorted(fun(num), reverse=True)
    print(len(ans))
    print(" ".join(map(str, ans)))
