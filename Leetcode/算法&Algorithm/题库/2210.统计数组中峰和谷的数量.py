class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = []
        nums = deque(nums)
        while nums:
            cur = nums.popleft()
            if not res:
                res.append(cur)
            else:
                if res[-1] == cur:
                    continue
                else:
                    res.append(cur)
        ans = 0
        for i in range(1, len(res) - 1):
            if (res[i - 1] < res[i]) == (res[i] > res[i + 1]):
                ans += 1
        return ans
