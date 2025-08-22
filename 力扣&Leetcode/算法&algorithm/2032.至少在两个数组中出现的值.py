class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        nums = nums1 + nums2 + nums3
        cnt = Counter(nums)
        return [i for i, j in cnt.items() if j >= 2]
