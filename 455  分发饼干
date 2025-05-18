class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        nums1 = sorted(s, reverse=True)
        nums2 = sorted(g, reverse=True)
        satisfied_children = 0
        cookie_ptr = 0
        child_ptr = 0
        # 使用双指针法分配饼干
        while cookie_ptr < len(nums1) and child_ptr < len(nums2):
            if nums1[cookie_ptr] >= nums2[child_ptr]:
                satisfied_children += 1
                cookie_ptr += 1
                child_ptr += 1
            else:
                child_ptr += 1
        return satisfied_children
