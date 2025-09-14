class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        res = []
        for i in nums:
            if not res or res[-1][-1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        ans = 0
        for i, j in res:
            ans += j - i + 1
        return ans
