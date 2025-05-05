class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cur = 0
        left = right = 0
        cnt = defaultdict(int)
        n = len(s)
        while right < n:
            cnt[s[right]] += 1
            if cnt["0"] <= k or cnt["1"] <= k:
                cur += 1
                right += 1
            else:
                cnt.clear()
                left += 1
                right = left

            if right >= n:
                cnt.clear()
                left += 1
                right = left
            # print(s[left : right + 1], cur)
        return cur

from collections import defaultdict as dd


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cur = 0
        left = right = 0
        cnt = defaultdict(int)
        n = len(s)

        while right < n:
            cnt[s[right]] += 1
            while cnt["0"] > k and cnt["1"] > k:  # 如果窗口不满足条件，收缩左边界
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            cur += right - left + 1  # 统计以 right 为右边界的子串数量
            right += 1

        return cur
