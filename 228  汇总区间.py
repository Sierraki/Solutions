class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)  # 9
        left = 0
        list1 = []
        if n == 1:
            return [f"{nums[0]}"]
        else:
            for r in range(1, n):  # 1-9 但只会迭代到8
                if nums[r] - nums[r - 1] > 1 and r != n:  # r跟r左边的数超过1
                    if {nums[left]} == {nums[r - 1]}:
                        a = f"{nums[left]}"
                    if {nums[left]} != {nums[r - 1]}:
                        a = f"{nums[left]}->{nums[r-1]}"  # 提取区间
                    list1.append(a)

                    left = r
                if r == n - 1:
                    if {nums[left]} == {nums[r]}:
                        a = f"{nums[left]}"
                    if {nums[left]} != {nums[r]}:
                        a = f"{nums[left]}->{nums[r]}"
                    list1.append(a)
            return list1
