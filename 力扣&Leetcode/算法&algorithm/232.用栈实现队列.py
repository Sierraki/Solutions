class MyQueue:

    def __init__(self):
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> int:
        res = self.nums[0]
        del self.nums[0]
        return res

    def peek(self) -> int:
        return self.nums[0]

    def empty(self) -> bool:
        if not self.nums:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
