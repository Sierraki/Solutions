class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        heapq.heapify(nums)
        tar = [2, 3, 5]
        for i in range(n):
            cur = heapq.heappop(nums)
            for j in tar:
                if cur * j not in nums:
                    heapq.heappush(nums, cur * j)
        return cur
