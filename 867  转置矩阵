class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix[0])
        n2 = len(matrix)
        a = []
        for i in range(n):
            for j in range(n2):
                a.append(matrix[j][i])
        ele = []
        eles = []
        cnt = 0
        for i in a:
            ele.append(i)
            cnt += 1
            if cnt == len(matrix):
                cnt = 0
                eles.append(ele)
                ele = []
        return eles
