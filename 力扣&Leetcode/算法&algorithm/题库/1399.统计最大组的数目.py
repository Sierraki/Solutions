class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = defaultdict(list)

        def fun(n=int) -> int:
            res = [int(i) for i in str(n)]
            return sum(res)

        mx = 0
        for i in range(1, n + 1):
            cnt[fun(i)].append(i)
            mx = max(mx, len(cnt[fun(i)]))
        return sum([1 for i in cnt.values() if len(i) == mx])
