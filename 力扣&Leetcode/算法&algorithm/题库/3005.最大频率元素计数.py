class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return sum([cnt[i] for i in cnt.keys() if cnt[i] == max(cnt.values())])
