class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        a = 0.5
        b = numExchange - 1.5
        c = -numBottles
        delta = b * b - 4 * a * c
        ans = ceil((-b + sqrt(delta)) / (2 * a))
        return numBottles + ans - 1
