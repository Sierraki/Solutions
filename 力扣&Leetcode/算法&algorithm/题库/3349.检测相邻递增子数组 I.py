class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        l, r = 0, 1
        res = []
        while l <= r and r < len(nums):
            if nums[r - 1] < nums[r]:
                r += 1
            else:
                res.append([l, r - 1])
                l = r
                r = l + 1
        if l < len(nums):
            res.append([l, len(nums) - 1])
        res = [[i, j] for i, j in res if j - i + 1 >= k]
        for i in range(len(res)):
            if i >= 1 and res[i][0] - 1 == res[i - 1][1]:
                return True
            if res[i][1] - res[i][0] + 1 >= 2 * k:
                return True
        return False
