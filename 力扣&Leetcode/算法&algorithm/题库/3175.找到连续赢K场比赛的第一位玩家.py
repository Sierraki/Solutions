class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        res = Counter()
        for idx, i in enumerate(skills):
            res[i] = idx
        if k >= len(skills):
            return res[max(skills)]
        skills = deque(skills)
        cnt = Counter()
        while skills:
            cur = skills.popleft()
            if cur > skills[0]:
                a = skills.popleft()
                skills.append(a)
                cnt[cur] += 1
                if cnt[cur] == k:
                    ans = cur
                    break
                skills.appendleft(cur)
            else:
                cnt[cur] = 0
                cnt[skills[0]] += 1
                if cnt[skills[0]] == k:
                    ans = skills[0]
                    break
                skills.append(cur)
        return res[ans]
