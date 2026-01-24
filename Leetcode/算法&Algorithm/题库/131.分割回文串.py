class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        cur = []

        def check(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def backtracking(start):
            if start >= n:
                res.append(cur.copy())
                return
            for i in range(start, n):
                if check(s[start : i + 1]):
                    cur.append(s[start : i + 1])
                    backtracking(i + 1)
                    cur.pop()

        backtracking(0)
        return res
