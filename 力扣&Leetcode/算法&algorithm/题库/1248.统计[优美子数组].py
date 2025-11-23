class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i, j in enumerate(nums):
            if j % 2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0
        res = [0]
        s = 0
        for i in nums:
            s += i
            res.append(s)
        cnt = Counter()
        ans = 0
        for i in res:
            tar = i - k
            if tar not in cnt:
                cnt[i] += 1
            else:
                ans += cnt[tar]
                cnt[i] += 1
        return ans
