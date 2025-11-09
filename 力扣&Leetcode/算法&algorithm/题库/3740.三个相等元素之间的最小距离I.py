class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        for i, j in enumerate(nums):
            cnt[j].append(i)

        def fun(tar):
            ans = float("inf")
            for i in range(len(tar)):
                res = tar[i : i + 3]
                if len(res) == 3:
                    # print(res,2*(res[-1]-res[0]))
                    ans = min(ans, 2 * (res[-1] - res[0]))
            return ans

        ans = float("inf")
        for i in cnt.values():
            ans = min((fun(i)), ans)
        if ans == float("inf"):
            return -1
        return ans
