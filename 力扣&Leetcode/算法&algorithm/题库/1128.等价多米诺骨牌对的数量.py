class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def fun(a=list):
            res = str(a[0]) + "0" + str(a[1])
            return int(res)

        cnt = Counter()
        for i in dominoes:
            a = sorted(i)
            cnt[fun(a)] += 1
        ans = 0
        for i, j in cnt.items():
            if j >= 2:
                ans += (j - 1) * j // 2
        return ans
