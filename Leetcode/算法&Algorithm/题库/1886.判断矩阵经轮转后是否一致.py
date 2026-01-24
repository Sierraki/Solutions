class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # 90
        res1 = []
        for i in range(len(mat[0])):
            cnt = 0
            a = []
            for j in mat:
                a.append(j[i])
                cnt += 1
                if cnt == len(mat[0]):
                    res1.append(a[::-1])
                    break
        # 180
        res2 = []
        for i in range(n - 1, -1, -1):
            res2.append(mat[i][::-1])
        # 270
        res3 = []
        for i in range(n - 1, -1, -1):
            res3.append(res1[i][::-1])
        return target in [mat, res1, res2, res3]
