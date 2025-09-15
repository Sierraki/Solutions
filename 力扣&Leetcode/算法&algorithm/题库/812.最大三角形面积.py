class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # 面积
        def fun(a, b, c):
            a1, a2, b1, b2, c1, c2 = a[0], a[1], b[0], b[1], c[0], c[1]
            a = sqrt((a1 - b1) ** 2 + (a2 - b2) ** 2)
            b = sqrt((a1 - c1) ** 2 + (a2 - c2) ** 2)
            c = sqrt((b1 - c1) ** 2 + (b2 - c2) ** 2)
            p = (a + b + c) / 2
            return p * (p - a) * (p - b) * (p - c)

        ans = -float("inf")
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    ans = max(ans, fun(points[i], points[j], points[k]))
        return sqrt(ans)
