class Solution:
    def reverseBits(self, num: int) -> int:
        if num == 0:
            return 1
        res = bin(num & 0xFFFFFFFF)[2:]
        nums = [int(i) for i in str(res)]
        nums.insert(0, 0)
        l = r = 0
        cnt = Counter()
        mx = -float("inf")
        while l <= r and r < len(nums):
            cnt[nums[r]] += 1
            if cnt[0] <= 1:
                r += 1
                mx = max(mx, min(32, r - l))
            else:
                cnt[nums[l]] -= 1
                l += 1
                r += 1
        return mx
