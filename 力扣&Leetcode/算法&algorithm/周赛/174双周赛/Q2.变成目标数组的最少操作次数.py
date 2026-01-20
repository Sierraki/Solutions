class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        cnt = Counter()
        if nums == target:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] not in cnt:
                    if nums[i] != target[i]:
                        cnt[nums[i]] += 1
            return len(cnt)
