import sys
import bisect

input = sys.stdin.readline
data = sys.stdin.read().split()

n = int(data[0])
q = int(data[1])
nums = sorted(list(set(int(data[i]) for i in range(2, n + 2))))
ques = []
for k in range(q):
    ques.append([int(data[n + 2 + 2 * k]), int(data[n + 2 + 2 * k + 1])])
n = len(nums)
h = [nums[i] - i for i in range(n)]
ans = []
for i, j in ques:
    cnt = bisect.bisect_left(nums, i)
    pre = i - cnt
    target = pre + j

    idx = bisect.bisect_left(h, target)
    if idx == n:
        res = nums[-1] + (target - h[-1])
    else:
        res = nums[idx] - (h[idx] - target + 1)
    ans.append(str(res))
    print(res)
