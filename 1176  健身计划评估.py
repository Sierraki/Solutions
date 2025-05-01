class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        nums = calories
        n = len(calories)

        s = 0
        cur = sum(nums[:k])

        if cur < lower:
            s -= 1
        elif cur > upper:
            s += 1

        for i in range(1, n - k + 1):
            cur = cur + nums[i + k - 1] - nums[i - 1]

            if cur < lower:
                s -= 1
            elif cur > upper:
                s += 1
        return s
