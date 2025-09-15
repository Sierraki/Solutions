class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        nums = deque([i for i in range(num)])
        while len(nums) != 1:
            nums.rotate(-target + 1)
            nums.popleft()
        return nums[0]