class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        vis = [False] * n
        for i in initial:
            vis[i] = True

        def dfs(cur, path):
            path.append(cur)
            vis[cur] = True
            for i, j in enumerate(graph[cur]):
                if j == 1 and not vis[i]:
                    dfs(i, path)

        res = []
        for i in range(n):
            if not vis[i]:
                path = []
                dfs(i, path)
                res.append(path[:])
        head_v = defaultdict(list)
        for i in initial:
            for idx, j in enumerate(graph[i]):
                if j == 1:
                    head_v[i].append(idx)
        v_head = defaultdict(list)
        for i, j in head_v.items():
            for k in j:
                if k != i:
                    v_head[k].append(i)
        initial = set(initial)
        ans1 = Counter()
        for i in res:
            cnt1 = set()
            for j in i:
                for k in v_head[j]:
                    if k in initial:
                        cnt1.add(k)
            if len(cnt1) == 1:
                cnt1 = list(cnt1)
                ans1[cnt1[0]] += len(i)
        ans1 = [[i, j] for i, j in ans1.items()]
        ans1.sort(key=lambda x: (-x[1], x[0]))
        if ans1:
            return ans1[0][0]
        return min(initial)
