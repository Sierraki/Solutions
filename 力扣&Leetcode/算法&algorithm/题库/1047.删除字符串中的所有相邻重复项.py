class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        s = deque([i for i in s])
        while s:
            cur = s.popleft()
            if not res:
                res.append(cur)
            else:
                if res[-1] == cur:
                    res.pop()
                else:
                    res.append(cur)
        return "".join(res)
