class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def fun(nums=list, tar=list) -> bool:
            for i in range(len(tar)):
                if tar[i] == 0:
                    if not (nums[i] == nums[i + 1]):
                        return False
                elif tar[i] == 1:
                    if not (nums[i] < nums[i + 1]):
                        return False
                elif tar[i] == -1:
                    if not (nums[i] > nums[i + 1]):
                        return False
            return True

        # 1 < 0= -1>
        ans = 0
        for i in range(len(pattern), len(nums)):
            if fun(nums[i - len(pattern) : i + 1], pattern):
                ans += 1
        return ans
