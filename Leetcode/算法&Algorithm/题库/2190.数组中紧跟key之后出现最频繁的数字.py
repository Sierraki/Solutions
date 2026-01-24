class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        a = []
        for idx, i in enumerate(nums):
            if i == key and idx != len(nums) - 1:
                a.append(nums[idx + 1])
        a.sort()
        big = a[0]
        big_cnt = 0
        cur = a[0]
        cnt = 1
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                cur = a[i]
                cnt += 1
                if cnt > big_cnt:
                    big_cnt = cnt
                    big = cur
            else:
                cur = a[i]
                cnt = 1
        return big
