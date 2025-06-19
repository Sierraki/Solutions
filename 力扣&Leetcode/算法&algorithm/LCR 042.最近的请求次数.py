class RecentCounter(object):

    def __init__(self):
        self.nums = []

    def ping(self, t):
        # search left
        self.nums.append(t)
        lc = bisect.bisect_left(self.nums, t - 3000)
        return len(self.nums[lc:])


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
