class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        n = len(s2)
        stat = False

        for i in s1:
            dict1[i] += 1

        if len(s2) >= len(s1):
            for i in range(k):
                dict2[s2[i]] += 1

            if dict1 == dict2:
                stat = True

            for i in range(k, n):
                dict2[s2[i]] += 1
                dict2[s2[i - k]] -= 1
                if dict2[s2[i - k]] == 0:
                    del dict2[s2[i - k]]
                if dict1 == dict2:
                    stat = True
                    break

        else:
            stat = False
        return stat
