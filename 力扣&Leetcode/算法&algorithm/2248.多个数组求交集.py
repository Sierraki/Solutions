class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i in nums:
            res += list(set(i))
        cnt = Counter(res)
        ans = []
        for i, j in cnt.items():
            if j >= len(nums):
                ans.append(i)
        ans.sort()
        return ans
