class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        tar1, tar2 = [], []
        for i in range(len(s)):
            if s[i] != goal[i]:
                tar1.append(s[i])
                tar2.append(goal[i])
                if len(tar1) > 2:
                    return False
        if not tar1:
            cnt = Counter(s)
            if max(cnt.values()) >= 2:
                return True
            return False
        return tar1 == tar2[::-1]
