class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def fun(nums=str) -> list:
            res = []
            pin = 0
            for i in range(1, len(nums)):
                if nums[i] != nums[pin]:
                    res.append([i - pin, nums[pin]])
                    pin = i
            if len(nums) > 0:
                res.append([len(nums) - pin, nums[pin]])
            return res

        res1 = fun(name)
        res2 = fun(typed)
        if len(res1) != len(res2):
            return False
        for i in range(len(res1)):
            if res1[i][1] == res2[i][1]:
                if res1[i][0] > res2[i][0]:
                    return False
            else:
                return False
        return True
