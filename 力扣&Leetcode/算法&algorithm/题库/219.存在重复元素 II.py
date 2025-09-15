class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        left = 0
        lens = len(nums)
        if k >= lens:  # 如果 k 大于等于数组长度，直接检查整个数组
            return len(nums) != len(set(nums))
        for right in range(lens):
            if right - left <= k:  # 窗口大小不超过 k 时
                if nums[right] in seen:  # 检查当前元素是否在 seen 中
                    return True
                seen.add(nums[right])  # 将当前元素加入 seen
            else:  # 窗口大小超过 k 时
                seen.remove(nums[left])  # 移除左边界元素
                left += 1  # 移动左边界
                if nums[right] in seen:  # 检查当前元素是否在 seen 中
                    return True
                seen.add(nums[right])  # 将当前元素加入 seen
        return False
