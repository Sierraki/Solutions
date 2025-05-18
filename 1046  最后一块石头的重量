class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.nums = stones
        n = len(self.nums)
        while n >= 3:
            self.nums.sort(reverse=True)
            if self.nums[0] == self.nums[1] and n >= 3:
                del self.nums[0]
                del self.nums[0]
                n -= 2
            elif self.nums[0] != self.nums[1] and n >= 2:
                self.nums[1] = self.nums[0] - self.nums[1]
                del self.nums[0]
                n -= 1
        if n == 1:
            return int(self.nums[0])
        else:
            if self.nums[0] == self.nums[1]:
                return 0
            else:
                return int(abs(self.nums[0] - self.nums[1]))
