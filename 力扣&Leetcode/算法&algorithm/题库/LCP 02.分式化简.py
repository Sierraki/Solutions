class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n, m = 0, 1
        for a in cont[::-1]:
            n, m = m, (m * a + n)
        return [m, n]
