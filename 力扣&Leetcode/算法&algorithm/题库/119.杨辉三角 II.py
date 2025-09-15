class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [1]
        cnt = 0
        res = [[1]]
        n = rowIndex + 1
        if n == 0:
            print([])
        else:
            while cnt < n - 1:
                b1 = a.copy() + [0]
                b2 = [0] + a.copy()
                new = []
                for i in range(len(b1)):
                    a = b1[i] + b2[i]
                    new.append(a)
                a = new
                cnt += 1
            return a
