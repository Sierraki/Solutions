class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        # 有多少个点
        pos = []
        for i in range(rows):
            for j in range(cols):
                pos.append([i, j])

        # 每个点到中心的距离
        def fun(x=int, y=int, tar=list) -> int:
            return abs(tar[0] - x) + abs(tar[1] - y)

        # 排序
        for i in range(len(pos)):
            pos[i] = [fun(rCenter, cCenter, pos[i]), pos[i]]
        pos.sort(key=lambda x: x[0])
        return [i[1] for i in pos]
