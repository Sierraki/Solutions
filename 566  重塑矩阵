class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        un = []
        for i in mat:
            for j in i:
                un.append(j)
        a = []
        b = []
        rcnt = 0
        ccnt = 0
        if len(un) != r * c:
            return mat
        else:
            while rcnt < r:
                for i in un:
                    b.append(i)
                    ccnt += 1
                    if ccnt == c:
                        a.append(b)
                        b = []
                        ccnt = 0
                        rcnt += 1
            return a
