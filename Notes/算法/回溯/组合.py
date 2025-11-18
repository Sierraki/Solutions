nums = [1, 2, 3, 4]


res = []
n = len(nums)
k = 2


def backtarck(start=int, cur=list):
    if len(cur) == k:
        # 限制长度k
        res.append(cur.copy())
        return

    for i in range(start, n):
        cur.append(nums[i])
        backtarck(i + 1, cur)
        cur.pop()


backtarck(0, [])
print(res)
