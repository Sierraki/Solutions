class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = nums.copy()
        res.sort()
        nums = deque(nums)
        res = deque(res)
        cnt = 0
        while nums:
            if res[-1] > nums[0]:
                cnt += 1
                res.pop()
                nums.popleft()
            else:
                nums.popleft()
        return cnt
