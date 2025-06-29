class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if not array:
            return []
        result = []
        top, bottom = 0, len(array) - 1
        left, right = 0, len(array[0]) - 1
        while top <= bottom and left <= right:
            # 从左到右
            for col in range(left, right + 1):
                result.append(array[top][col])
            top += 1
            # 从上到下
            for row in range(top, bottom + 1):
                result.append(array[row][right])
            right -= 1
            # 从右到左
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(array[bottom][col])
                bottom -= 1
            # 从下到上
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(array[row][left])
                left += 1
        return result
