class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        tar = ['a', 'b', 'c']
        res = []

        def dfs(cur):
            if len(cur) == n:
                res.append(''.join(cur))
                return
            for i in tar:
                if not cur or i != cur[-1]:
                    cur.append(i)
                    dfs(cur)
                    cur.pop()
        dfs([])
        if k > len(res):
            return ''
        return res[k - 1]
