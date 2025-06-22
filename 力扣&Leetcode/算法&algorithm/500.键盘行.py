class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        cnt = Counter()
        for i in r1:
            cnt[i] += 1
        for i in r2:
            cnt[i] += 2
        for i in r3:
            cnt[i] += 3
        res = []
        for i in words:
            res1 = [j for j in i]
            for idx, j in enumerate(res1):
                res1[idx] = cnt[j.lower()]
            res.append(res1)
        ans = []
        for idx, i in enumerate(res):
            if len(Counter(i)) == 1:
                ans.append(words[idx])
        return ans
