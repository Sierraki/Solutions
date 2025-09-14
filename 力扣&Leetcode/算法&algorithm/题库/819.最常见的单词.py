class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        a = re.sub(r"[^a-zA-Z]", " ", paragraph)
        a = a.split(" ")
        for i in range(len(a)):
            a[i] = a[i].lower()
        cnt = Counter(a)
        # print(cnt)
        d = [" ", ""] + banned
        # print(d)
        for i in d:
            if i in cnt:
                del cnt[i]
        print(cnt)
        b = max(cnt, key=lambda k: cnt[k])
        return b
