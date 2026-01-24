class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        a = nums[0]
        b = nums[-1]
        cnt = Counter(nums)
        res = [i for i in cnt.keys() if cnt[i] == 1]
        if k == 1:
            if not res:
                return -1
            return max(res)
        else:
            if k == len(nums):
                return max(nums)
            if cnt[a] > 1 and cnt[b] > 1:
                return -1
            elif cnt[a] > 1 and cnt[b] == 1:
                return b
            elif cnt[a] == 1 and cnt[b] > 1:
                return a
            elif cnt[a] == 1 and cnt[b] == 1 and a != b:
                return max(a, b)
            elif cnt[a] == 1 and cnt[b] == 1 and a == b:
                return -1
