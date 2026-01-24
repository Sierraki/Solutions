class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if target[0] == 1:
            ans = ["Push"] * target[0]
        else:
            ans = ["Push"] * (target[0] - 1) + ["Pop"] * (target[0] - 1) + ["Push"]
        for i in range(1, len(target)):
            ans += (
                ["Push"] * (target[i] - target[i - 1] - 1)
                + ["Pop"] * (target[i] - target[i - 1] - 1)
                + ["Push"]
            )
        return ans
