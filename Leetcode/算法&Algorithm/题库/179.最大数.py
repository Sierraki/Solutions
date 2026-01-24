class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for _ in range(n):
            for i in range(1, n):
                p1 = str(nums[i - 1]) + str(nums[i])
                p2 = str(nums[i]) + str(nums[i - 1])
                if int(p2) > int(p1):
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]

        return str(int("".join(map(str, nums))))
