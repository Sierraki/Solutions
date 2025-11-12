class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def bt(start=int, cur=list):
            if len(cur) == k:
                if sum(cur) == n:
                    res.append(cur.copy())
                return
                # 结束当前
            if 10 - start < k - len(cur):
                return
                # 结束当前
            for i in range(start, 10):
                cur.append(i)
                bt(i + 1, cur)
                cur.pop()

        res = []
        bt(1, [])
        return res
