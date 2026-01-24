class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        dif1 = abs(int(coordinate1[1]) - int(coordinate2[1]))
        dif2 = abs(ord(coordinate1[0]) - ord(coordinate2[0]))
        return (dif1 + dif2) % 2 == 0
