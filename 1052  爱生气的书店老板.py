class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        nums = customers
        g = grumpy
        k = minutes
        n = len(nums)
        s = 0
        for i in range(n):
            if g[i] == 0:
                s += nums[i]
        w = 0
        for i in range(k):
            if g[i] == 1:
                w += nums[i]
        big = w
        for i in range(k, n):
            if g[i] == 1:
                w += nums[i]
            if g[i - k] == 1:
                w -= nums[i - k]
            big = max(w, big)
        return(big + s)

