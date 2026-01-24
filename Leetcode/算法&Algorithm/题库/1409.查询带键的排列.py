class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        nums = [i for i in range(1, m + 1)]
        a = []
        for i in queries:
            lc = nums.index(i)
            a.append(lc)
            tar = nums[lc]
            del nums[lc]
            nums.insert(0, tar)
        return a
