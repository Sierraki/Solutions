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


# 你的风格：极简快速读入
input = sys.stdin.readline


def fun(n, k, s):
    # 找到所有 '1' 的索引
    ones = [i for i, char in enumerate(s) if char == "1"]

    # 1. 全是 '0' 的特殊情况
    if not ones:
        return (n + k) // (k + 1)

    ans = 0
    # 2. 开头部分：第一个 '1' 左边的 0
    ans += ones[0] // (k + 1)

    # 3. 中间部分：每两个 '1' 之间的 0
    for i in range(len(ones) - 1):
        gap = ones[i + 1] - ones[i] - 1
        ans += max(0, (gap - k) // (k + 1))

    # 4. 结尾部分：最后一个 '1' 右边的 0
    ans += (n - 1 - ones[-1]) // (k + 1)

    return ans


# 直接开始主循环，不要 if __name__
size_line = input().strip()
if size_line:
    for _ in range(int(size_line)):
        # 兼容读取 n, k
        nk = input().split()
        if not nk:
            continue
        n, k = map(int, nk)

        # 读取字符串并去掉换行符
        s = input().strip()

        print(fun(n, k, s))
