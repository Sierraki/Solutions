class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # 合并区间
        if len(ranges) == 1:
            return 2
        ranges.sort()
        ranges = deque(ranges)
        res = []
        while ranges:
            if not res:
                cur = ranges.popleft()
                res.append(cur)
            if res[-1][1] >= ranges[0][0]:
                res[-1][1] = max(ranges[0][1], res[-1][1])
                ranges.popleft()
            else:
                cur = ranges.popleft()
                res.append(cur)
        return (2 ** len(res)) % (10**9 + 7)
