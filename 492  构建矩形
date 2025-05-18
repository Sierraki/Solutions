class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(1, floor(sqrt(area)) + 1):
            # print(i)
            if area % i == 0:
                ans = i
        a = [ans, int(area / ans)]
        a.sort(reverse=True)
        return a
