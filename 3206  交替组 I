class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        target1 = [1, 0, 1]
        target2 = [0, 1, 0]
        cnt = 0
        colors += colors[:2]
        for i in range(2, len(colors)):
            a = colors[i - 2 : i + 1]
            if a == target1 or a == target2:
                cnt += 1
        return cnt
