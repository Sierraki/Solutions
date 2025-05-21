class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        #注意房子的可用高度。只降不增
        box_len = len(boxes)
        house_len = len(warehouse)

        ava_house = [0 for _ in range(house_len)]
        ava_h = float('inf')
        for i in range(house_len):
            if ava_h > warehouse[i]:
                ava_h = warehouse[i]
            ava_house[i] = ava_h
        
        boxes.sort()
        b_i = 0         #箱子从小到大，尝试往房子里塞
        for i in range(house_len - 1, -1, -1):  #房子从右往左，从小到大，尝试消耗
            if boxes[b_i] <= ava_house[i]:  #能装得下的情况
                b_i += 1
            if b_i >= box_len:  #箱子都装完了
                break
            else:
                continue
        
        return b_i