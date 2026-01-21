class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        ans = 0
        n = len(nums)
        res = []
        for i in range((n)):
            heapq.heappush(res, -nums[i])
            if s[i] == "1":
                ans += heapq.heappop(res)
        return -ans
