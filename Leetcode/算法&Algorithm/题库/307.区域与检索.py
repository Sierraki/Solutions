class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(0, 0, self.n - 1, nums)

    def _build(self, node, left, right, nums):
        if left == right:
            self.tree[node] = nums[left]
            return
        mid = (left + right) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        self._build(left_node, left, mid, nums)
        self._build(right_node, mid + 1, right, nums)
        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def update(self, index: int, val: int) -> None:
        if self.n > 0:
            self._update(0, 0, self.n - 1, index, val)

    def _update(self, node, left, right, idx, val):
        if left == right:
            self.tree[node] = val
            return
        mid = (left + right) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        if idx <= mid:
            self._update(left_node, left, mid, idx, val)
        else:
            self._update(right_node, mid + 1, right, idx, val)
        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def sumRange(self, left: int, right: int) -> int:
        if self.n == 0:
            return 0
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, left, right, L, R):
        if L <= left and right <= R:
            return self.tree[node]
        mid = (left + right) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        res = 0
        if L <= mid:
            res += self._query(left_node, left, mid, L, R)
        if R > mid:
            res += self._query(right_node, mid + 1, right, L, R)
        return res
