class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur = deque([])
        ans = []
        for i, j in enumerate(nums):
            if cur and cur[0] <= i - k:
                cur.popleft()
            while cur and nums[cur[-1]] <= j:
                cur.pop()
            cur.append(i)
            if i >= k - 1:
                ans.append(nums[cur[0]])
        return ans
