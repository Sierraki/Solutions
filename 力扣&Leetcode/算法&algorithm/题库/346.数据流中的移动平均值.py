class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.l1 = []
        self.left = 0

    def next(self, val: int) -> float:
        self.l1.append(val)
        if len(self.l1) > self.size:
            self.l1.pop(0)

        return sum(self.l1) / len(self.l1)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
