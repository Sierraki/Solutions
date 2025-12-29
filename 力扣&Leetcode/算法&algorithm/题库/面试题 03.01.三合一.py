class TripleInOne:

    def __init__(self, stackSize: int):
        self.nums = [[] * stackSize for _ in range(3)]
        self.n = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.nums[stackNum]) < self.n:
            self.nums[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if len(self.nums[stackNum]) > 0:
            cur = self.nums[stackNum][-1]
            self.nums[stackNum].pop()
            return cur
        return -1

    def peek(self, stackNum: int) -> int:
        if len(self.nums[stackNum]) > 0:
            return self.nums[stackNum][-1]
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.nums[stackNum] == []


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
