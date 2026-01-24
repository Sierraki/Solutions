class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def bt(start=int, cur=list):
            if len(cur) == k:
                res.append(cur.copy())
                return
                # 结束当前
            if n + 1 - start < k - len(cur):
                return
                # 结束当前
            for i in range(start, n + 1):
                cur.append(i)
                bt(i + 1, cur)
                cur.pop()

        bt(1, [])
        return res
