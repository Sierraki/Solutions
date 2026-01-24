class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        cnt = Counter(nums)
        return len(nums) % k == 0 and max(cnt.values()) <= len(nums) // k
