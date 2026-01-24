class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def fun(cur, left, right):
            if len(cur) == 2 * n:
                res.append("".join(cur.copy()))
                return
            if left < n:
                cur.append("(")
                fun(cur, left + 1, right)
                cur.pop()
            if right < left:
                cur.append(")")
                fun(cur, left, right + 1)
                cur.pop()

        fun([], 0, 0)
        return res
