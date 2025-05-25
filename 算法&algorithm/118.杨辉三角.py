class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [1]
        cnt = 0
        res = [[1]]
        n = numRows
        if n == 0:
            return []
        else:
            while cnt < n - 1:
                b1 = a.copy() + [0]
                b2 = [0] + a.copy()
                new = []
                for i in range(len(b1)):
                    a = b1[i] + b2[i]
                    new.append(a)
                a = new
                res.append(a)
                cnt += 1
            return res
