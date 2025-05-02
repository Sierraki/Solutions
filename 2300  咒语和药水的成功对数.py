class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        nums = potions
        n = len(nums)

        for i in range(len(spells)):
            left = 0
            right = n - 1
            mid = (left + right) // 2

            target = success / spells[i]

            while left <= right:
                if target > nums[right]:
                    spells[i] = 0
                    break
                else:

                    if target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid

                    mid = (left + right) // 2
                    if left == mid == right:
                        spells[i] = n - left
                        break
        return spells
