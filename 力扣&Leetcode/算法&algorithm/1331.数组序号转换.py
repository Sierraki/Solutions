class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = [[idx, i] for idx, i in enumerate(arr)]
        nums.sort(key=lambda x: x[1])
        for idx, i in enumerate(nums):
            if idx == 0:
                nums[idx].append(1)
            else:
                if nums[idx][1] == nums[idx - 1][1]:
                    nums[idx].append(nums[idx - 1][2])
                elif nums[idx][1] > nums[idx - 1][1]:
                    nums[idx].append(nums[idx - 1][2] + 1)
        nums.sort(key=lambda x: x[0])
        res = [i[2] for i in nums]
        return res
