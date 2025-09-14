class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        nums = data
        k = sum(data)

        s = cur = sum(nums[:k])

        for i in range(k, n):
            cur += nums[i] - nums[i - k]
            s = max(s, cur)

        return k - s
