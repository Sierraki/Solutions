class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # [ ]
        n = len(nums)
        l = 0
        r = n - 1
        a = -1
        b = -1
        if nums == []:
            return [a, b]
        elif nums != []:

            if target > nums[r] or target < nums[l]:
                return [a, b]
            else:
                while l < r:
                    m = (r + l) // 2
                    if target <= nums[m]:
                        r = m
                    else:
                        l = m + 1
                    if l == r:
                        break
                a = l

                l = 0
                r = n - 1

                while l < r:

                    if target >= nums[m]:
                        l = m
                    else:
                        r = m - 1
                    m = (r + l) // 2
                    if m == l:
                        break
                b = m

                return (a, b)
