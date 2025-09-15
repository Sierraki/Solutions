class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for idx, i in enumerate(mat):
            res.append([idx, i.count(1)])
        res.sort(key=lambda x: x[1])
        return [res[i][0] for i in range(k)]
