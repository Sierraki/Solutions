class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        # N=7, 4*7=28, 足够安全
        self.tree = [0] * (4 * self.n)

        if self.n > 0:
            self._build(0, 0, self.n - 1)

    # 1. 建树：自底向上
    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
            return

        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2

        self._build(left, start, mid)
        self._build(right, mid + 1, end)
        self.tree[node] = self.tree[left] + self.tree[right]

    # 2. 更新：单点修改
    def update(self, idx, val):
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            self.nums[idx] = val
            return

        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2

        if idx <= mid:
            self._update(left, start, mid, idx, val)
        else:
            self._update(right, mid + 1, end, idx, val)

        self.tree[node] = self.tree[left] + self.tree[right]

    # 3. 查询：区间求和
    def query(self, L, R):
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        if L <= start and end <= R:
            return self.tree[node]

        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        res = 0

        if L <= mid:
            res += self._query(left, start, mid, L, R)
        if R > mid:
            res += self._query(right, mid + 1, end, L, R)

        return res


# 测试 N=7
nums = [1, 3, 5, 7, 9, 11, 13]
st = SegmentTree(nums)
print(f"原始和 [2, 5]: {st.query(2, 5)}")  # 应该输出 32 (5+7+9+11)

st.update(2, 6)  # 把 5 改成 6
print(f"更新后 [2, 5]: {st.query(2, 5)}")  # 应该输出 33
