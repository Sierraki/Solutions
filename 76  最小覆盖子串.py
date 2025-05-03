from collections import Counter, defaultdict


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


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # 计数器记录 t 中每个字符的需求数量
        cnt = Counter(t)
        required = len(cnt)  # 需要满足的不同字符种类数

        left = right = 0
        n = len(s)
        formed = 0  # 当前窗口中满足需求的字符种类数
        window_counts = defaultdict(int)

        # 最小窗口长度、起始位置
        min_len = float("inf")
        result = (0, 0)  # 窗口起止索引

        while right < n:
            char = s[right]
            if char in cnt:
                window_counts[char] += 1

                # 如果当前字符的数量刚好满足要求
                if window_counts[char] == cnt[char]:
                    formed += 1

            # 尝试收缩窗口
            while formed == required:
                # 更新最小窗口
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = (left, right)

                # 移动左指针
                char_left = s[left]
                if char_left in cnt:
                    window_counts[char_left] -= 1
                    if window_counts[char_left] < cnt[char_left]:
                        formed -= 1
                left += 1

            right += 1

        return "" if min_len == float("inf") else s[result[0] : result[1] + 1]
