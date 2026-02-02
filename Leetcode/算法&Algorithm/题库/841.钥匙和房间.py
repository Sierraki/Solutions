class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = [False] * n

        def dfs(cur):
            vis[cur] = True
            for i in rooms[cur]:
                if not vis[i]:
                    dfs(i)

        dfs(0)
        for i in vis:
            if not i:
                return False
        return True
