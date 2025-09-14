class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.nums.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.nums:
            tar = self.nums[0]
            del self.nums[0]
            return tar

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.nums[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.nums:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
