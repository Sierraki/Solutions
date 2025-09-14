class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = sum(apple)
        capacity.sort(reverse=True)
        tar = 0
        pin = 0
        while tar < n:
            tar += capacity[pin]
            pin += 1
        return pin


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = sum(apple)
        tar = 0
        cnt = 0
        while tar < n:
            tar += max(capacity)
            cnt += 1
            lc = capacity.index(max(capacity))
            del capacity[lc]
        return cnt


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = sum(apple)
        capacity.sort(reverse=True)
        prefix_sum = []
        total = 0
        for cap in capacity:
            total += cap
            prefix_sum.append(total)
        left, right = 0, len(prefix_sum)
        while left < right:
            mid = (left + right) // 2
            if prefix_sum[mid] >= n:
                right = mid
            else:
                left = mid + 1
        return left + 1
