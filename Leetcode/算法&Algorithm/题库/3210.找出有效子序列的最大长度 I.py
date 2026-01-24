class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter()
        odd = True
        odd_len = 0
        even = True
        even_len = 0
        for i in nums:
            if i % 2 == 1:
                if odd == True:
                    odd_len += 1
                    odd = False
                if even == False:
                    even_len += 1
                    even = True
                cnt[1] += 1
            else:
                if odd == False:
                    odd_len += 1
                    odd = True
                if even == True:
                    even_len += 1
                    even = False
                cnt[0] += 1
        return max(cnt[1], cnt[0], odd_len, even_len)
