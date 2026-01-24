from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # cnt里面最少的数次数不超过k
        cnt = defaultdict(int)
        left = mx = 0
        for right in range(len(s)):
            cnt[s[right]] += 1
            target = max(cnt.values())
            # 当前窗口长度减去最大频率字符的数量 > k，说明需要移动左指针
            while (right - left + 1 - target) > k:
                cnt[s[left]] -= 1
                left += 1
            mx = max(mx, right - left + 1)
        return mx


eg = Solution()
print(eg.characterReplacement("ABAB", 2))  # 4
print(eg.characterReplacement("AABABBA", 1))  # 4
print(
    eg.characterReplacement(
        "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF",
        4,
    )
)  # 7
