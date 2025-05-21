class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        cnt = Counter(questions)
        a = [i for i in cnt.values()]
        a.sort(reverse=True)
        print(a)
        cur = 0
        for idx, i in enumerate(a):
            cur += i
            if cur >= len(questions) // 2:
                return idx + 1
        return len(questions) // 2
