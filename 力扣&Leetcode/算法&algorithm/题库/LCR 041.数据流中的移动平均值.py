class MovingAverage(object):

    def __init__(self, size):
        self.n = 0
        self.nums = []
        self.size = size
        self.cnt = 0

    def next(self, val):
        if self.n >= self.size:
            self.cnt -= self.nums[0]
            del self.nums[0]
            self.n -= 1
        self.nums.append(val)
        self.cnt += val
        self.n += 1
        return float(self.cnt) / self.n
