class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans1 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = 0
                cnt = 0
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        if 0 <= i + a < m and 0 <= j + b < n:
                            ans += img[i + a][j + b]
                            cnt += 1
                ans1[i][j] = ans // cnt
        return ans1
