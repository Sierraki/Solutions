from collections import defaultdict


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 窗口内元素，频次最小的要小于等于k
        cnt = defaultdict(int)
        left = mx = 0
        for idx, right in enumerate(answerKey):
            cnt[right] += 1
            target = max(cnt.values())
            while idx - left + 1 - target > k:
                cnt[answerKey[left]] -= 1
                if cnt[answerKey[left]] == 0:
                    del cnt[answerKey[left]]
                left += 1
            mx = max(mx, idx - left + 1)
        return mx
