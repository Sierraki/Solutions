class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        k = len(p)

        n = len(s)
        a=[]

        for i in p:
            d2[i] += 1

        for i in range(n):
            if i < k:
                d1[s[i]] += 1
            else:
                d1[s[i]] += 1
                d1[s[i - k]] -= 1
                if d1[s[i - k]] == 0:
                    del d1[s[i - k]]
            if d1 == d2:
                a.append(i - k + 1)

        return(a)