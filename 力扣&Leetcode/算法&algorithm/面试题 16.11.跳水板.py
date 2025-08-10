class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        res = set()
        for i in range(k + 1):
            res.add(shorter * i + longer * (k - i))
        if sum(res) == 0:
            return []
        return sorted(list(res))
