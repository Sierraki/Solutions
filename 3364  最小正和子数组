class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        len_range = [i for i in range(l, r + 1)]
        n = len(nums)
        b = []
        for i in len_range:
            for j in range(n - i + 1):
                if sum(nums[j : j + i]) > 0:
                    b.append(nums[j : j + i])
        c = [sum(i) for i in b]
        c.sort()
        if c == []:
            return -1
        else:
            return c[0]
