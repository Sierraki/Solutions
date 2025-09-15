class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        nums = deque(original)
        res = []
        while nums:
            for _ in range(m):
                a = [0] * n
                for i in range(n):
                    cur = nums.popleft()
                    a[i] = cur
                res.append(a)
        return res
