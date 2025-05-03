from collections import defaultdict
import bisect


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        #转换开灯时间
        n = len(bulbs)
        nums = [0] * n
        for idx, i in enumerate(bulbs, start=1):
            nums[i - 1] = idx
        ans = -1
        k += 2
        a = sorted(nums[:k])
        mi = float("inf")
        if nums[0] in a[:2] and nums[k - 1] in a[:2]:
            mi = ans = max(a[:2])
        if k > n:
            return ans
        else:
            for i in range(k, n):
                # 寻找删除元素在a的索引
                lc = bisect.bisect_left(a, nums[i - k])
                # 删除元素
                a.pop(lc)
                # 加入元素
                bisect.insort(a, nums[i])
                # return(a, nums[i - k], nums[i])
                # 判断
                if nums[i] in a[:2] and nums[i - k + 1] in a[:2]:
                    ans = max(a[:2])
                    mi = min(ans, mi)
        if mi == float("inf"):
            return -1
        else:
            return mi
