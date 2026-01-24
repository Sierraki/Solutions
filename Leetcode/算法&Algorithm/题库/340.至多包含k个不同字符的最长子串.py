from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = mx = 0
        for idx, right in enumerate(s):
            cnt[right] += 1
            while len(cnt) > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            mx = max(mx, idx - left + 1)
        return mx


eg = Solution()
print(eg.lengthOfLongestSubstringKDistinct("eceba", 2))  # 3
print(eg.lengthOfLongestSubstringKDistinct("aa", 1))  # 2
