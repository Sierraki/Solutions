class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False  # 每个回文串至少需要一个字符
        count = Counter(s)
        odd_count = sum(1 for freq in count.values() if freq % 2 == 1)
        return odd_count <= k
