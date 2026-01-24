class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        # 对称
        cnt1 = Counter()
        # 不对称
        cnt2 = Counter()
        ans = 0
        res1 = ""
        res2 = 0
        for i in cnt:
            if i[::-1] in cnt and (i != i[::-1]) and i[::-1] not in cnt2:
                cnt2[i] = min(cnt[i], cnt[i[::-1]])
            elif i not in cnt1 and i == i[::-1]:
                cnt1[i] = cnt[i]
        for i, j in cnt1.items():
            if j % 2 == 1:
                if len(i) > len(res1):
                    res2 = len(i)
                    res1 = i
                ans += len(i) * (j - 1)
            else:
                ans += len(i) * j
        ans += res2
        for i, j in cnt2.items():
            ans += len(i) * 2 * j
        return ans
