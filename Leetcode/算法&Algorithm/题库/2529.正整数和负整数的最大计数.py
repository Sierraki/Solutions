class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = 0

        r = n - 1
        cnt = a = b = 0

        for i in range(n):
            if nums[i] < 0:
                cnt += 1
            else:
                break
        a = cnt
        cnt = 0

        while r >= 0:
            if nums[r] > 0:
                cnt += 1
                r -= 1
            else:
                break
        b = cnt

        return max(a, b)
