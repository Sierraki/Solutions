class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.nums.sort(reverse=True)
        while len(self.nums) > k:
            self.nums.pop()

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
