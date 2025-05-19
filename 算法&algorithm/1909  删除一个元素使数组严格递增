from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        a = nums.copy()
        b = nums.copy()
        sta = True
        stb = True
        if n == 2:
            return True
        elif n == 3:
            if nums[1] - nums[0] > 0 or nums[2] - nums[1] > 0:
                return True
            else:
                return False
        else:
            for i in range(1, n):
                if nums[i] - nums[i - 1] <= 0:
                    target = i
                    del a[target]
                    del b[target - 1]
                    for i in range(1, n - 1):
                        if a[i] - a[i - 1] <= 0:
                            sta = False
                            break
                    for i in range(1, n - 1):
                        if b[i] - b[i - 1] <= 0:
                            stb = False
                            break
                    break
            if sta == True or stb == True:
                return True
            elif sta == False and stb == False:
                return False
