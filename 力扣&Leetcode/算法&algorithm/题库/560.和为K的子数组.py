class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        s = 0
        for i in nums:
            s += i
            prefix.append(s)
        cnt = Counter()
        ans = 0
        for i in prefix:
            tar = i - k
            if tar in cnt:
                ans += cnt[tar]
            cnt[i] += 1
            if i == k:
                ans += 1
        return ans
