class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = []
        for i in candies:
            if i + extraCandies >= max(candies):
                l.append(True)
            else:
                l.append(False)
        return l
