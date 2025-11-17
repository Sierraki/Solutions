class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        nums = [(1 if i.isdigit() else -1) for i in array]
        prefix = []
        s = 0
        for i in nums:
            s += i
            prefix.append(s)
        maps = defaultdict(list)
        for i, j in enumerate(prefix):
            maps[j].append(i)
        res = []
        mx = 1
        # 区间左右端点
        left = right = 0
        for i, j in maps.items():
            if i != 0:
                if len(j) > 1:
                    left = j[0] + 1
                    right = j[-1]
            else:
                left = 0
                right = j[-1]
            mx = max(mx, right - left + 1)
            res.append([left, right])
        if mx == 1:
            return []
        # 筛选出符合最长长度的区间
        ans = []
        for i, j in res:
            if j - i + 1 == mx:
                ans.append([i, j])
        ans.sort()
        return array[ans[0][0] : ans[0][1] + 1]
