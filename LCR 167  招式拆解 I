class Solution:
    def dismantlingAction(self, arr: str) -> int:
        left = right = mx = 0
        cnt = Counter()
        while right < len(arr):
            cnt[arr[right]] += 1
            # move windows
            if max(cnt.values()) >= 2:
                cnt[arr[left]] -= 1
                left += 1
                right += 1
            # add element
            else:
                right += 1
                mx = max(mx, right - left)
        return mx
