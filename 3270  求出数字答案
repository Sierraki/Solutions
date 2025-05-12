class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [str(num1), str(num2), str(num3)]
        for i in range(len(nums)):
            nums[i] = nums[i].zfill(4)
        # print(nums)
        a = []
        for i in range(len(nums[0])):
            mi = 9
            for j in nums:
                mi = min(mi, int(j[i]))
            a.append(mi)
        # print(a)
        b = "".join(map(str, a))
        return int(b)
