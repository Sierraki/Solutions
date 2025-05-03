from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        k = len(t)
        left = right = 0
        mi = n
        if k > n:
            return ""
        else:
            cnt = Counter(t)
            # return(dict(cnt))
            st = False
            # 移动right指针
            while left <= right and right < n:
                # 移动右指针
                while max(cnt.values()) > 0 and right < n:
                    if s[right] in cnt:
                        cnt[s[right]] -= 1
                    right += 1
                # 移动左指针
                while max(cnt.values()) <= 0:
                    st = True
                    if right - left <= mi:
                        mi = right - left
                        ans = s[left:right]
                    # return(cnt, mi, s[left:right])
                    if left < right and s[left] in cnt:
                        cnt[s[left]] += 1
                    left += 1
        if st == False:
            return ""
        else:
            return ans
