class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        nums = [i[-1] / i[0] for i in rectangles]
        cnt = defaultdict(int)
        s = 0
        for i in nums:
            cnt[i] += 1
        for key, i in cnt.items():
            s = s + (i) * (i - 1) / 2
        return int(s)
