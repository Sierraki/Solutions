class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        n = len(guess)
        cnt = 0
        for i in range(n):
            if guess[i] == answer[i]:
                cnt += 1
        return cnt
