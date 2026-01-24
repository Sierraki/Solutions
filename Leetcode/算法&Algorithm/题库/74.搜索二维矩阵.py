class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find(nums=list[int]):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if target >= nums[mid]:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        nums = [i[0] for i in matrix]
        return matrix[find(nums)][find(matrix[find(nums)])] == target
