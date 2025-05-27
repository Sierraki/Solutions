class Solution:
    def maxSubstrings(self, word: str) -> int:
        cnt = defaultdict(list)
        for idx, i in enumerate(word):
            cnt[i].append(idx)
        res = []
        for k in cnt:
            nums = cnt[k]
            for i in range(len(nums)):
                target = nums[i] + 3
                j = bisect.bisect_left(nums, target, i + 1)
                if j < len(nums):
                    res.append((nums[i], nums[j]))
        res.sort(key=lambda x: x[1])
        le = -1
        cntt = 0
        for start, end in res:
            if start > le:
                cntt += 1
                le = end
        return cntt
