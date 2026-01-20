import sys

input = sys.stdin.readline
n, tar = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]


def fun(n, tar, nums):
    pf = [[0] * (tar + 1) for _ in range(n + 1)]
    for i in range(n):
        w, v = nums[i]
        for j in range(tar + 1):
            pf[i + 1][j] = pf[i][j]
            if j >= w:
                if pf[i][j - w] + v > pf[i + 1][j]:
                    pf[i + 1][j] = pf[i][j - w] + v
    suf = [[0] * (tar + 2) for _ in range(n + 2)]
    for i in range(n, 0, -1):
        w, v = nums[i - 1]
        for j in range(tar + 1):
            suf[i][j] = suf[i + 1][j]
            if j >= w:
                if suf[i + 1][j - w] + v > suf[i][j]:
                    suf[i][j] = suf[i + 1][j - w] + v
    v1mx = pf[n][tar]
    for i in range(n + 1):
        for j in range(1, tar + 1):
            if pf[i][j - 1] > pf[i][j]:
                pf[i][j] = pf[i][j - 1]
    for i in range(n + 2):
        for j in range(1, tar + 1):
            if suf[i][j - 1] > suf[i][j]:
                suf[i][j] = suf[i][j - 1]
    ans = ""
    for i in range(1, n + 1):
        w, v = nums[i - 1]
        v2mx = -1
        for j in range(tar - w + 1):
            v2mx = max(v2mx, pf[i - 1][j] + suf[i + 1][tar - w - j] + v)
        if v2mx < v1mx:
            ans += "C"
        else:
            v3 = -1
            for j in range(tar + 1):
                v3 = max(v3, pf[i - 1][j] + suf[i + 1][tar - j])
            if v3 < v1mx:
                ans += "A"
            else:
                ans += "B"
    return ans


print((fun(n, tar, nums)))
