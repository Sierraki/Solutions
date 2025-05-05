from collections import defaultdict

s = "10101"
k = 1

cnt = defaultdict(int)
left = right = 0
n = len(s)
cnt[s[0]] += 1
cur = 0
while right <n:
    # 移动左
    if min(cnt.values()) <= k:
        cur += 1
        left += 1
    # 移动右
    else:
        right += 1

    print(cur)
