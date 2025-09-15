class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        cnt = Counter(nums)
        if cnt[n] == 2:
            cnt[n] -= 1
            if len(cnt) == n and max(cnt.values()) == min(cnt.values()) == 1:
                return True
        return False
