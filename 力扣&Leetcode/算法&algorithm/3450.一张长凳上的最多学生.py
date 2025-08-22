class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        mx = 0
        cnt = defaultdict(set)
        for i, j in students:
            cnt[j].add(i)
            mx = max(mx, len(cnt[j]))
        return mx
