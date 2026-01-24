class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter()
        for idx, i in enumerate(nums2):
            if i not in cnt:
                cnt[i] = idx
        res = []
        for i in nums1:
            res.append(cnt[i])
        return res
