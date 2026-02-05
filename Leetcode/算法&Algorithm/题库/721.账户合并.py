class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = 0
        mail_idx = defaultdict()
        mail_idx1 = defaultdict()
        pin = 0
        for i in accounts:
            cur = i[1:]
            for j in cur:
                if j not in mail_idx:
                    mail_idx[j] = pin
                    mail_idx1[pin] = j
                    pin += 1
                    n = pin
        au = len(accounts)
        graph = []
        for i in accounts:
            cur = i[1:]
            res = []
            for j in cur:
                res.append(mail_idx[j])
            graph.append(res)
        adj = [[] * n for _ in range(n)]
        for i in graph:
            for a in range(len(i)):
                for b in range(a + 1, len(i)):
                    adj[i[a]].append(i[b])
                    adj[i[b]].append(i[a])
        vis = [False] * n
        res = []

        def dfs(cur, path):
            path.append(cur)
            vis[cur] = True
            for i in adj[cur]:
                if not vis[i]:
                    dfs(i, path)

        for i in range(n):
            if not vis[i]:
                path = []
                dfs(i, path)
                res.append(path)
        idx_mail = defaultdict()
        for i in accounts:
            cur = i[1:]
            for j in cur:
                idx_mail[mail_idx[j]] = i[0]
        ans = []
        for i in res:
            cur = []
            for j in i:
                cur.append(mail_idx1[j])
            ans.append([idx_mail[i[0]]] + sorted(cur))
        return ans
