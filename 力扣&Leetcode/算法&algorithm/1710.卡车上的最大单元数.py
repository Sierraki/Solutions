class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        nums = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ans = 0
        for i in nums:
            if truckSize >= i[0]:
                truckSize -= i[0]
                ans += i[0] * i[1]
            else:
                ans += truckSize * i[1]
                break
        return ans
