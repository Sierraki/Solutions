class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            return (x * 2 + z) * 2
        return (min(x, y) * 2 + z + 1) * 2
