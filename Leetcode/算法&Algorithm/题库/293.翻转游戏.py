class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        nums = [i for i in currentState]
        res = []
        for idx, i in enumerate(nums):
            if idx > 0:
                if nums[idx - 1] == i == "+":
                    nums[idx - 1] = nums[idx] = "-"
                    ans = "".join(nums)
                    res.append(ans)
                    nums[idx - 1] = nums[idx] = "+"
        return res
