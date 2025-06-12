class Solution:
    def minMaxDifference(self, num: int) -> int:
        mi = float("inf")
        mx = -1
        nums = [i for i in str(num)]
        check = list(set(nums))
        for i in check:
            cop = nums.copy()
            for j in range(len(cop)):
                if cop[j] == i:
                    cop[j] = "0"
            mi = min(mi, int("".join(cop)))
        for i in check:
            cop = nums.copy()
            for j in range(len(cop)):
                if cop[j] == i:
                    cop[j] = "9"
            mx = max(mx, int("".join(cop)))
        return mx - mi
