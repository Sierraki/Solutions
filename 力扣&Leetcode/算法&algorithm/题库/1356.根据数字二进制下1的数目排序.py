class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        for i in arr:
            res.append([i, bin(i).count("1")])
        res.sort(key=lambda x: (x[1], x[0]))
        return [i[0] for i in res]
