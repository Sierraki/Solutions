class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        target = s - x
        n = len(nums)
        
        # 如果目标值为0，说明不需要任何操作
        if target == 0:
            return n
        
        # 如果目标值小于0，说明无法通过移除元素达到目标
        if target < 0:
            return -1
        
        # 使用滑动窗口来找到最长的子数组，其和为target
        max_len = -1
        cur_sum = 0
        left = 0
        
        for right in range(n):
            cur_sum += nums[right]
            
            while cur_sum > target and left <= right:
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
        
        # 如果找到了这样的子数组，返回最小操作数
        return n - max_len if max_len != -1 else -1