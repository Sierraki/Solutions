class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums) // 2
        a = deque(nums[:n])
        b = deque(nums[n:])
        cnt = 0
        while a and b:
            if a[-1] * 2 <= b[-1] or b[-1] * 2 <= a[-1]:
                cnt += 2
                a.pop()
                b.pop()
            else:
                if a[-1] > b[-1]:
                    a.pop()
                else:
                    b.pop()
        return cnt
