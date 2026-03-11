class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k = len(nums[0])
        tar = set(nums)

        def dfs(cur):
            if len(cur) == k:
                if cur not in tar:
                    return cur
                return
            res1 = dfs(cur + "1")
            if res1:
                return res1
            res2 = dfs(cur + "0")
            if res2:
                return res2
            return

        return dfs("")
