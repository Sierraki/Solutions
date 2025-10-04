class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return 1
            else:
                return -1
        t = defaultdict(set)
        bt = defaultdict(set)
        for i, j in trust:
            t[i].add(j)
            bt[j].add(i)
        # 被n-1信任的人
        for i, j in bt.items():
            if len(j) == n - 1:
                if i not in t:
                    return i
        return -1
