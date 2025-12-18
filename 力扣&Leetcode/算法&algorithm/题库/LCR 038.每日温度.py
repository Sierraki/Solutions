class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = deque([])
        p = [0] * len(temperatures)
        for idx, i in enumerate(temperatures):
            if not res:
                res.append([i, idx])
            else:
                while res and i > res[0][0]:
                    cur = res.popleft()
                    p[cur[1]] = idx - cur[1]
                while res and i > res[-1][0]:
                    cur = res.pop()
                    p[cur[1]] = idx - cur[1]
                if res and i > res[0][0]:
                    res.append([i, idx])
                else:
                    res.appendleft([i, idx])
        return p
