class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        mi = float("inf")
        for idx, i in enumerate(warehouse):
            mi = min(mi, i)
            warehouse[idx] = mi
        boxes.sort()
        cnt = 0
        top = len(warehouse) - 1
        dow = 0
        while dow < (len(boxes)) and top >= 0:
            if boxes[dow] <= warehouse[top]:
                cnt += 1
                dow += 1
                top -= 1
            else:
                top -= 1
        return cnt
