class Solution:
    def maximumBeauty(self, items, queries):
        items.sort()
        # 处理更新价格
        a = [0] * len(queries)
        mx = 0
        for i in range(len(items)):
            mx = max(items[i][1], mx)
            items[i][1] = mx
        res = 0
        for j in range(len(queries)):
            left, right = 0, len(items) - 1
            mid = (left + right) // 2

            while left <= right:
                if queries[j] >= items[mid][0]:
                    res = items[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2

            a[j] = res

        return a
