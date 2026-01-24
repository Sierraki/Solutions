import bisect
from sortedcontainers import SortedList
from collections import defaultdict, Counter


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4
        cnt = Counter(s)
        left = 0
        mi = float("inf")
        if max(cnt.values()) == k and len(cnt) == 4:
            return 0
        for right in range(left, n):
            cnt[s[right]] -= 1
            while max(cnt.values()) <= k:
                cur = right - left + 1
                mi = min(mi, cur)
                cnt[s[left]] += 1
                left += 1
        return mi


eg = Solution()
print(eg.balancedString("QWER"))  # 0
print(eg.balancedString("QQWE"))  # 1
print(eg.balancedString("QQQW"))  # 2
print(eg.balancedString("WWEQERQWQWWRWWERQWEQ"))  # 4
