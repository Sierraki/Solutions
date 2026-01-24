class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idxx = []
        for idx, i in enumerate(nums):
            if i == key:
                idxx.append(idx)
        a = []
        for i in idxx:
            for j in range(i - k, i + k + 1):
                if j >= 0 and j <= len(nums) - 1:
                    a.append(j)
        return list(set(a))
