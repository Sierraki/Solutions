class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        cnt = defaultdict(list)
        for idx, i in enumerate(arr):
            cnt[i].append(idx)
        self.cnt = cnt

    def query(self, left: int, right: int, value: int) -> int:
        target = self.cnt[value]
        lc1 = bisect_left(target, left)
        lc2 = bisect_right(target, right)
        return lc2 - lc1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
