class FrontMiddleBackQueue:

    def __init__(self):
        self.nums = []
        self.n = 0

    def pushFront(self, val: int) -> None:
        self.nums.insert(0, val)
        self.n += 1
        # print(self.nums)

    def pushMiddle(self, val: int) -> None:
        self.nums.insert(self.n // 2, val)
        self.n += 1
        # print(self.nums)

    def pushBack(self, val: int) -> None:
        self.nums.append(val)
        self.n += 1
        # print(self.nums)

    def popFront(self) -> int:
        num = -1
        if self.n > 0:
            num = self.nums[0]
            del self.nums[0]
            self.n -= 1
        # print(self.nums,num)
        return num

    def popMiddle(self) -> int:
        num = -1
        if self.n > 0:
            num = self.nums[(self.n - 1) // 2]
            del self.nums[(self.n - 1) // 2]
            self.n -= 1
        # print(self.nums,num)
        return num

    def popBack(self) -> int:
        num = -1
        if self.n > 0:
            num = self.nums[-1]
            del self.nums[-1]
            self.n -= 1
        # print(self.nums,num)
        return num


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
