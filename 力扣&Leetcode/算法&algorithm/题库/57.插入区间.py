class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]
        while intervals:
            if res[-1][-1] >= intervals[0][0]:
                res[-1][-1] = max(res[-1][-1], intervals[0][1])
            else:
                res.append(intervals[0])
            del intervals[0]
        return res
