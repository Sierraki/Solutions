class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        n = len(s)
        s = [s[i] for i in range(n)]

        if k>n:
            return 0
        else:

            cnt = defaultdict(int)
            c = 0
            for i in range(k):
                cnt[s[i]] += 1
            if len(cnt) == k:
                c += 1

            for i in range(k, n):

                cnt[s[i]] += 1
                cnt[s[i - k]] -= 1
                if cnt[s[i - k]] == 0:
                    del cnt[s[i - k]]
                if len(cnt) == k:
                    c += 1

            return(c)