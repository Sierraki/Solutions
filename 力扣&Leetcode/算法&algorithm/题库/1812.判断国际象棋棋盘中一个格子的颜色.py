class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        p1 = coordinates[:1]
        p2 = int(coordinates[1:])
        if ord(p1) % 2 == p2 % 2:
            return False
        else:
            return True
