class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        a = [[i, j] for i, j in cnt.items()]
        a.sort()
        mx = 0
        for i in range(1, len(a)):
            if a[i][0] - a[i - 1][0] == 1:
                mx = max(mx, a[i][1] + a[i - 1][1])
        return mx
