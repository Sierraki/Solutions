class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        tar = [i.lower() for i in licensePlate if i.isalpha()]
        res = list(set(tar))
        cnt = Counter(tar)
        mi = float("inf")
        for i in words:
            c1 = Counter(i)
            for j in res:
                if cnt[j] > c1[j]:
                    break
            else:
                if len(i) < mi:
                    ans = i
                    mi = len(i)
        return ans
