class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        def fun(a: int, b: int):
            if a < b:
                for i in range(a + 1, b + 1):
                    cnt[i] += 1
            else:
                for i in range(1, b + 1):
                    cnt[i] += 1
                for i in range(a + 1, n + 1):
                    cnt[i] += 1

        cnt = Counter([i for i in range(1, n + 1)])
        cnt[rounds[0]] += 1
        for i in range(1, len(rounds)):
            fun(rounds[i - 1], rounds[i])
        tar = max(cnt.values())
        return [i for i in cnt.keys() if cnt[i] == tar]
