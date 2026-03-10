class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k = len(nums[0])
        res = []
        swap = [True]
        tar = set(nums)

        def dfs(cur):
            if swap[0]:
                if len(cur) == k:
                    if cur not in tar:
                        res.append(cur)
                        swap[0] = False
                    return
                dfs(cur + "1")
                dfs(cur + "0")

        dfs("")
        return res[0]
