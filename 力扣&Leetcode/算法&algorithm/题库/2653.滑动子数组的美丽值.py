from typing import List
import bisect
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        a = sorted(nums[:k])
        res = [a[x - 1] if a[x - 1] < 0 else 0]
        for i in range(k, n):
            # 移除窗口最左边元素（对应原数组中 nums[i-k]）
            lc = bisect.bisect_left(a, nums[i - k])
            del a[lc]
            # 插入新元素保持有序
            bisect.insort(a, nums[i])
            # 记录当前窗口第 x 小元素
            res.append(a[x - 1] if a[x - 1] < 0 else 0)
        return res
