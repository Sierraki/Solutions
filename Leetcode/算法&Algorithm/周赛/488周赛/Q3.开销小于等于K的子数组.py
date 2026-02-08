class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = deque([])
        mi = deque([])
        l = 0
        cnt = 0
        for r in range(n):
            while mx and nums[mx[-1]] <= nums[r]:
                mx.pop()
            mx.append(r)
            while mi and nums[mi[-1]] >= nums[r]:
                mi.pop()
            mi.append(r)
            while True:
                cur_mx = nums[mx[0]]
                cur_mi = nums[mi[0]]
                le = r - l + 1
                cost = (cur_mx - cur_mi) * le
                if cost <= k:
                    break
                if mx[0] == l:
                    mx.popleft()
                if mi[0] == l:
                    mi.popleft()
                l += 1
                if l > r:
                    break
            cnt += r - l + 1
        return cnt
