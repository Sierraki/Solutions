class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        po = ne = 0
        swap = True
        for i, j in enumerate(nums, 1):
            if j % 2 == 1:
                if swap == True:
                    swap = False
                else:
                    swap = True
            if i % 6 == 0:
                if swap == True:
                    swap = False
                else:
                    swap = True
            if swap:
                po += j
            else:
                ne += j
        return po-ne
