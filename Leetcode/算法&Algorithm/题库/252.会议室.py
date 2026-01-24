class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < intervals[i - 1][-1]:
                return False
        else:
            return True
