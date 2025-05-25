class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        a = self.nums2[index]
        self.nums2[index] += val
        b = self.nums2[index]
        self.cnt[a] -= 1
        if self.cnt[a] < 0:
            del self.cnt[a]
        self.cnt[b] += 1

    def count(self, tot: int) -> int:
        res = 0
        for i in self.nums1:
            target = tot - i
            if target in self.cnt:
                res += self.cnt[target]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
