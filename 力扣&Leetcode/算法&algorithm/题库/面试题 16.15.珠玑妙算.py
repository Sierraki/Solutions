class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        ans1 = ans2 = 0
        cnt1 = Counter(solution)
        cnt2 = Counter(guess)
        for i in range(4):
            if solution[i] == guess[i]:
                ans1 += 1
                if solution[i] in cnt1:
                    cnt1[solution[i]] -= 1
                    if cnt1[solution[i]] == 0:
                        del cnt1[solution[i]]
                if guess[i] in cnt1:
                    cnt2[guess[i]] -= 1
                    if cnt2[guess[i]] == 0:
                        del cnt2[guess[i]]
        for i in cnt2.keys():
            if i in cnt1:
                if cnt2[i] >= cnt1[i]:
                    ans2 += cnt1[i]
                else:
                    ans2 += cnt2[i]
        return [ans1, ans2]
