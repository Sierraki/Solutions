class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        list1 = [i for i in range(1, n + 1)]
        list1.sort()
        nums = list(set(nums))
        nums.sort()

        t = 0
        d = 0

        a = []

        while t <= n - 1:
            if list1[t] == nums[d]:
                t += 1
                if d + 1 < len(nums):
                    d += 1
            else:
                a.append(list1[t])
                t += 1


        return a