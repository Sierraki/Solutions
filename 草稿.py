from sortedcontainers import SortedList as sl  # 修正类名大小写

bulbs = [6, 5, 8, 9, 7, 1, 10, 2, 3, 4]
k = 2
n = len(bulbs)
# 转换数组
nums = [0] * n
for idx, i in enumerate(bulbs, start=1):
    nums[i - 1] = idx
print(nums)
# 进入判断
k += 2
a = sl(nums[:k])
ans = cur = float("inf")
if nums[0] in a[:2] and nums[k] in a[:2]:
    ans = cur = max(a[:2])

for i in range(k, n):
    # 加入元素nums[i]
    a.add(nums[i])
    # 删除元素nums[i-k]
    a.remove(nums[i - k])
    # 判断两端点，nums[i],nums[i-k+1]
    if nums[i] in a[:2] and nums[i - k + 1] in a[:2]:
        cur = max(a[:2])
        ans = min(ans, cur)
if ans==float("inf"):
    return -1
else:
    return ans
