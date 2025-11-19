class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        nums = deque([])
        ans = [i for i in s]
        for i, j in enumerate(s):
            if j in "()":
                nums.append([j, i])
        res = []
        goal = set()
        while nums:
            cur = nums.popleft()
            if cur[0] == "(":
                res.append(cur)
            else:
                if res:
                    if res[-1][0] == "(":
                        res.pop()
                    else:
                        goal.add(cur[-1])
                else:
                    goal.add(cur[-1])
        for i in res:
            goal.add(i[-1])
        for i in range(len(ans) - 1, -1, -1):
            if i in goal:
                del ans[i]
        return "".join(ans)
