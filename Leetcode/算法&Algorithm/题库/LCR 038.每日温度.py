class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        res = []
        for idx, i in enumerate(temperatures):
            if not res:
                res.append(idx)
            else:
                while res and i > temperatures[res[-1]]:
                    ans[res[-1]] = idx - res[-1]
                    res.pop()
                res.append(idx)
        return ans
