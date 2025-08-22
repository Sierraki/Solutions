class Solution:
    def isPathCrossing(self, path: str) -> bool:
        res = [[0, 0]]
        po = [0, 0]
        for i in path:
            if i == "N":
                po[0] += 1
            elif i == "S":
                po[0] -= 1
            elif i == "W":
                po[1] -= 1
            elif i == "E":
                po[1] += 1
            if po in res:
                return True
            res.append(po[:])
        return False
