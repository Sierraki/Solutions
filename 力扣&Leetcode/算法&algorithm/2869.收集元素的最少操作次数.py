class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        for i in range(1, k + 1):
            cnt[i] += 1
        nums = nums[::-1]
        for idx, i in enumerate(nums):
            if i in cnt:
                cnt[i] -= 1
            if max(cnt.values()) == 0:
                return idx + 1
