class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        def check(s1, s2):
            # 左下角
            # max（左下角的x坐标）
            # max（左下角的y坐标）
            x1 = max(s1[0][0], s2[0][0])
            y1 = max(s1[0][1], s2[0][1])
            # 右上角
            # min（右上角的x坐标）
            # min（右上角的y坐标）
            x2 = min(s1[1][0], s2[1][0])
            y2 = min(s1[1][1], s2[1][1])
            if y1 > y2 or x1 > x2:
                return 0
            return min((y2 - y1), (x2 - x1))

        ans = 0
        for i in range(len(bottomLeft) - 1):
            # print(bottomLeft[i], topRight[i])
            for j in range(i + 1, len(bottomLeft)):
                tar = [[bottomLeft[i], topRight[i]], [bottomLeft[j], topRight[j]]]
                ans = max(ans, check(tar[0], tar[1]))
        return (ans) ** 2
