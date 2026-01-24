class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        nums = "0"
        for i in arr:
            nums += str(i) + "0"
        for i in range(m * 2, len(nums), 2):
            tar = nums[i + 1 - 2 * m : i + 1] * k
            if tar in nums:
                return True
        return False
