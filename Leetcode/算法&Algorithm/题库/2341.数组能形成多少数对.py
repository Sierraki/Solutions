class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        a = 0
        b = 0
        for i in cnt.values():
            a += i // 2
            b += i % 2
        return [a, b]
