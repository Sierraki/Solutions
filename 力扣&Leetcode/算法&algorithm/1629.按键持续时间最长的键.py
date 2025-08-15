class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = [0] * len(releaseTimes)
        res[0] = releaseTimes[0]
        for i in range(1, len(res)):
            res[i] = releaseTimes[i] - releaseTimes[i - 1]
        cnt = Counter()
        for i in range(len(res)):
            cnt[keysPressed[i]] = max(cnt[keysPressed[i]], res[i])
        tar = max(cnt.values())
        ans = "a"
        for i, j in cnt.items():
            if j == tar:
                ans = chr(max(ord(ans), ord(i)))
        return ans
