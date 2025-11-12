class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tar = n - k % n
        for _ in range(tar):
            nums.append(nums[0])
            del nums[0]
