class Solution:
    def makeFancyString(self, s: str) -> str:
        res = deque([])
        s = deque([i for i in s])
        while s:
            cur = s.popleft()
            if len(res) < 2:
                res.append(cur)
            else:
                if res[-1] == res[-2] == cur:
                    continue
                else:
                    res.append(cur)
        return "".join(res)
