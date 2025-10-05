class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        def fun(nums=list) -> list:
            res = []
            for i in range(len(nums)):
                if i == 0 or i == len(nums) - 1:
                    res.append(nums[i])
                if 0 < i < len(nums) - 1:
                    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                        res.append(nums[i] - 1)
                    elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                        res.append(nums[i] + 1)
                    else:
                        res.append(nums[i])
            return res

        last = arr.copy()
        cur = fun(arr)
        while cur != last:
            last = cur
            cur = fun(cur)
        return cur
