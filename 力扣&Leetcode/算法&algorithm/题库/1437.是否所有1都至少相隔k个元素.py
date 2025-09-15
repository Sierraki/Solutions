class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        list1 = []
        for a, b in enumerate(nums):
            if b == 1:
                list1.append(a)
        list2 = []
        for i in range(1, len(list1)):
            list2.append(list1[i] - list1[i - 1] - 1)
        if nums.count(1) <= 1:
            return True
        return min(list2) == k
