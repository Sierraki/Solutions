class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        k = minSize
        n = len(s)
        cnt = defaultdict(int)

        print(dict(cnt))

        for i in range(k - 1, n):
            a = s[i - k + 1 : i + 1]
            if len(set(a)) <= maxLetters:
                cnt[a] += 1
        return(max(cnt.values()) if cnt else 0)
