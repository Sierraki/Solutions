class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        cnt = defaultdict(int)
    
        wl = 0
        one = zero = 0
        for i in range(n):
            if (cnt[0] == k and nums[i] == 1) or cnt[0] < k:  # 长度+1
                cnt[nums[i]] += 1
                wl += 1
                one = cnt[1]
                zero = cnt[0]
            elif cnt[0] > k or (cnt[0] == k and nums[i] == 0):  # 窗口移动
                cnt[nums[i]] += 1
                cnt[nums[i - wl]] -= 1
                if cnt[nums[i - wl]] == 0:
                    del cnt[nums[i - wl]]

            #return(dict(cnt), nums[i - wl + 1 : i + 1], one, zero)

        return(one + zero)
        
