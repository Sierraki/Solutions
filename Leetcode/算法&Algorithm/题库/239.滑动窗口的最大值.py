class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = deque([])
        ans = []
        for i in range(len(nums)):
            if not res:
                res.append(nums[i])
            else:
                if nums[i - k] >= res[0] and i - k >= 0:
                    res.popleft()
                if res:
                    while res and nums[i] > res[-1]:
                        res.pop()
                res.append(nums[i])
            if i >= k - 1:
                ans.append(res[0])
        return ans

