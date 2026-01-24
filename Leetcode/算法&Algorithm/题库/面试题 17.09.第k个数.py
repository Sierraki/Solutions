class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        nums = [1]
        heapq.heapify(nums)
        cnt = set([1])
        for i in range(k - 1):
            cur = nums[0]
            heapq.heappop(nums)
            res = [cur * 3, cur * 5, cur * 7]
            for j in res:
                if j not in cnt:
                    cnt.add(j)
                    heapq.heappush(nums, j)
        return nums[0]
