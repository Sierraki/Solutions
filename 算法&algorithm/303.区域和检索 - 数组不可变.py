class NumArray:

    def __init__(self, nums: List[int]):
        self.list1 = [0]
        self.nums = nums
        self.n = len(self.nums)
        for i in range(self.n):
            a = self.nums[i] + self.list1[i]
            self.list1.append(a)

    def sumRange(self, left: int, right: int) -> int:
        return self.list1[right + 1] - self.list1[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
