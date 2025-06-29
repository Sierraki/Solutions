class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)
        self.k = k

    def add(self, val: int) -> int:
        def fun(nums: list, target: int) -> int:
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        lc = fun(self.nums, val)
        if lc == -1:
            self.nums.append(val)
        else:
            self.nums.insert(lc, val)
        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
