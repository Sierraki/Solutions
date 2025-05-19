class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        f = sum(arr[:k])
        target = k * threshold

        cur = f
        cnt = 0
        if cur >= target:
            cnt += 1

        for i in range(k, len(arr)):

            cur = arr[i] - arr[i - k] + cur
            if cur >= target:
                cnt += 1
        return cnt
