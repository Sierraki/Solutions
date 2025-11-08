class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        a = []
        b = []
        for i, j in enumerate(team):
            if j == 1:
                a.append(i)
            else:
                b.append(i)
        top = down = 0
        ans = 0
        while top < len(a) and down < len(b):
            if abs(b[down] - a[top]) <= dist:
                ans += 1
                top += 1
                down += 1
            else:
                if b[down] > a[top]:
                    top += 1
                else:
                    down += 1
        return ans
