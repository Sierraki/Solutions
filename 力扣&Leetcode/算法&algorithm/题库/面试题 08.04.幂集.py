class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for k in range(n + 1):

            def bt(pin, cur):
                if len(cur) == k:
                    res.append(cur.copy())
                    return
                for i in range(pin, n):
                    cur.append(nums[i])
                    bt(i + 1, cur)
                    cur.pop()

            bt(0, [])
        return res
