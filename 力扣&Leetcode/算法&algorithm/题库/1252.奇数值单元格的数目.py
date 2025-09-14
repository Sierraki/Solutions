class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        ma = [[0] * n for _ in range(m)]
        # print(ma)
        for i in indices:
            # row
            for j in range(n):
                ma[i[0]][j] += 1
                # print(ma[i[0]][j])
            # col
            for k in range(m):
                ma[k][i[-1]] += 1
        # print(ma)
        cnt = 0
        for i in ma:
            for j in i:
                if j % 2 == 1:
                    cnt += 1
        return cnt
