class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []  # sort
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.nums:
            self.nums.append(x)
        else:
            lc = bisect.bisect(self.nums, x)
            self.nums.insert(lc, x)

    def pop(self) -> None:
        tar = self.stack[-1]
        self.stack.pop()
        lc = bisect.bisect_left(self.nums, tar)
        del self.nums[lc]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.nums[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
