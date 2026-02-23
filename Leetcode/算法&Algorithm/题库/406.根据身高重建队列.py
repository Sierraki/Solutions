class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = [] * n
        for i in range(n):
            lc= people[i][1]
            ans.insert(lc, people[i])
        return ans
