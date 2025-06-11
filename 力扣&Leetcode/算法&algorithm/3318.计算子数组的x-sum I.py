class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def fun(nums: list, x: int):
            cnt = Counter(nums)
            res = [[i, j] for i, j in cnt.items()]
            res.sort(key=lambda x: (-x[1], -x[0]))
            ans = []
            tar = x
            for i in res:
                tar -= 1
                ans.append(i[0])
                if tar == 0:
                    break
            s = 0
            for i in nums:
                if i in ans:
                    s += i
            return s

        res = []
        for i in range(k - 1, len(nums)):
            ans = fun(nums[i - k + 1 : i + 1], x)
            res.append(ans)
        return res
