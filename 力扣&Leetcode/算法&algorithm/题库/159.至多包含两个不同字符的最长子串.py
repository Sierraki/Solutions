from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        cur = big = 0
        cnt = defaultdict(int)
        for i in s:
            cnt[i] += 1
            cur += 1
            while len(cnt) > 2:
                cnt[s[left]] -= 1
                cur -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            big = max(big, cur)
        return big

sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb"))   # 5 ("aabbb")
print(sol.lengthOfLongestSubstringTwoDistinct("abc"))       # 2 ("ab" 或 "bc")
print(sol.lengthOfLongestSubstringTwoDistinct("abaccc"))     # 4 ("accc")
print(sol.lengthOfLongestSubstringTwoDistinct("aaaaa"))      # 5
