class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
        n = len(nums)
        cnt = defaultdict(int)
        cur = 0
        big = 0


        for i in range(k):
            cnt[nums[i]] += 1
            cur += nums[i]
        # 字典初始化

        if len(cnt) >= m:
            big = cur

        for i in range(k, n):
            # add
            cnt[nums[i]] += 1
            cur += nums[i]
            # del
            cnt[nums[i - k]] -= 1
            cur -= nums[i - k]
            if cnt[nums[i - k]] == 0:
                del cnt[nums[i - k]]

            if len(cnt) >= m and cur > big:
                big = cur

        return(big)
