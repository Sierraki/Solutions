class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        co = []
        t = 0  # 上指针
        while t < len(nums1) and len(nums2) > 0:
            for i in range(len(nums2)):  # i 下指针
                if nums2[i] == nums1[t]:
                    co.append(nums2[i])
                    del nums1[t]
                    del nums2[i]
                    break  # 退出内层循环，重新检查 t 和 nums1
            else:
                t += 1  # 如果没有匹配，递增 t
        return co  # 输出最终结果
